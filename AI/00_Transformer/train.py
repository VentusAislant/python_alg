"""
利用手撕的 Transformer 训练一个对对子模型, 主要模块包括
    Seq2SeqDataset: 数据集类
    Tokenizer 使用 llama-2-7b-chat
    训练loop，使用 AdamW
"""
import os
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import torch.optim as optim
from transformers import AutoTokenizer
from .transformer import *

tokenizer_path = "/home/wind/Disks/16t/Models/LLMs/llama/llama-2-7b-chat"
max_model_len = 1024
batch_size = 64
train_file = "/home/wind/Disks/16t/Datasets/My/Duizi/annotations/train_data.csv"
d_model = 512
num_heads = 8
num_encoder_layers = 4
num_decoder_layers = 4
lr = 1e-5
epochs = 100
device = 'cuda:0'
save_dir = "./checkpoints"

os.makedirs(save_dir, exist_ok=True)

tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)
print(tokenizer)
vocab_size = len(tokenizer)
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token
if tokenizer.bos_token_id is None:
    tokenizer.bos_token_id = tokenizer.cls_token_id
if tokenizer.eos_token_id is None:
    tokenizer.eos_token_id = tokenizer.sep_token_id
decoder_start_token_id = tokenizer.bos_token_id
decoder_end_token_id = tokenizer.eos_token_id
print(decoder_start_token_id, decoder_end_token_id)


class Seq2SeqDataset(Dataset):
    def __init__(self, csv_file, tokenizer, max_len=128):
        """
        csv_file: train.csv 路径
        tokenizer: 用于将文本转换为 token id
        max_len: 最大序列长度
        """
        # 忽略 CSV 的第一列索引
        self.data = pd.read_csv(csv_file)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        src = self.data.iloc[idx]['up']
        tgt = self.data.iloc[idx]['down']

        src_ids = self.tokenizer(src, add_special_tokens=False)['input_ids'][:self.max_len]
        src_ids = torch.tensor(src_ids, dtype=torch.long)
        tgt_ids = self.tokenizer(tgt, add_special_tokens=True)['input_ids'][:self.max_len]
        tgt_ids += [self.tokenizer.eos_token_id]
        if len(tgt_ids) > self.max_len:
            tgt_ids = tgt_ids[:-1] + [self.tokenizer.eos_token_id]
        tgt_ids = torch.tensor(tgt_ids, dtype=torch.long)

        # print(src, tgt)
        # print(self.tokenizer.decode(src_ids), self.tokenizer.decode(tgt_ids))
        # print(src_ids, tgt_ids)
        # exit(0)

        # decoder_input_ids 和 labels
        decoder_input_ids = tgt_ids[:-1]  # 去掉最后一个 eos
        labels = tgt_ids[1:]              # 去掉第一个 bos

        return {
            "input_ids": src_ids,
            "decoder_input_ids": decoder_input_ids,
            "labels": labels
        }

# collate_fn 用于 pad
def collate_fn(batch, pad_token_id):
    # ===== 取出 =====
    input_ids = [item['input_ids'] for item in batch]
    decoder_input_ids = [item['decoder_input_ids'] for item in batch]
    labels = [item['labels'] for item in batch]

    # ===== padding =====
    input_ids = nn.utils.rnn.pad_sequence(
        input_ids,
        batch_first=True,
        padding_value=pad_token_id
    )
    decoder_input_ids = nn.utils.rnn.pad_sequence(
        decoder_input_ids,
        batch_first=True,
        padding_value=pad_token_id
    )
    labels = nn.utils.rnn.pad_sequence(
        labels,
        batch_first=True,
        padding_value=-100
    )

    # ===== encoder padding mask =====
    # [bsz, seq_len] -> [bsz, 1, 1, seq_len]
    encoder_mask = (input_ids != pad_token_id).unsqueeze(1).unsqueeze(2)

    # ===== decoder padding mask =====
    # causal mask 在 decoder layer 里构造
    # 这里只传 padding mask: [bsz, 1, 1, tgt_len]
    decoder_mask = (decoder_input_ids != pad_token_id).unsqueeze(1).unsqueeze(2)

    return {
        'input_ids': input_ids,
        'decoder_input_ids': decoder_input_ids,
        'labels': labels,
        'encoder_mask': encoder_mask,
        'decoder_mask': decoder_mask
    }

# 构建 dataset 和 dataloader
dataset = Seq2SeqDataset(train_file, tokenizer, max_len=max_model_len)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, collate_fn=lambda batch: collate_fn(batch, tokenizer.pad_token_id))


model = Transformer(num_encoder_layers, num_decoder_layers, vocab_size, d_model, num_heads, max_seq_len=max_model_len, device='cuda')

def init_weights(m):
    if isinstance(m, (torch.nn.Linear, torch.nn.Embedding)):
        torch.nn.init.xavier_uniform_(m.weight)
        if hasattr(m, 'bias') and m.bias is not None:
            torch.nn.init.zeros_(m.bias)
model.apply(init_weights)
model = model.to(device)

optimizer = optim.AdamW(model.parameters(), lr=lr)
criterion = nn.CrossEntropyLoss(ignore_index=-100)

for epoch in range(epochs):
    model.train()
    total_loss = 0

    for batch in dataloader:
        src = batch['input_ids'].to(device)
        decoder_input_ids = batch['decoder_input_ids'].to(device)
        labels = batch['labels'].to(device)
        encoder_mask = batch['encoder_mask'].to(device)
        decoder_mask = batch['decoder_mask'].to(device)

        optimizer.zero_grad()
        logits = model(src, decoder_input_ids, encoder_mask=encoder_mask, decoder_mask=decoder_mask)

        loss = criterion(logits.view(-1, vocab_size), labels.view(-1))
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(dataloader)
    print(f"Epoch {epoch}: loss={avg_loss:.4f}")

    if (epoch + 1) % 10 == 0:
        # 🔥 保存模型
        torch.save(
            model.state_dict(),
            f"{save_dir}/transformer_epoch_{epoch+1}.pt"
        )
