import torch
from transformers import AutoTokenizer
from .transformer import Transformer  # 你的手写模型

# ===== 配置 =====
device = "cuda:0"
tokenizer_path = "/home/wind/Disks/16t/Models/LLMs/llama/llama-2-7b-chat"
checkpoint_path = "./checkpoints/transformer_epoch_90.pt"

max_model_len = 1024
d_model = 512
num_heads = 8
num_encoder_layers = 4
num_decoder_layers = 4

# ===== tokenizer =====
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

# ===== model =====
model = Transformer(
    num_encoder_layers,
    num_decoder_layers,
    vocab_size,
    d_model,
    num_heads,
    max_seq_len=max_model_len,
    device=device
).to(device)

model.load_state_dict(torch.load(checkpoint_path, map_location=device))
model.eval()


def interactive_chat():
    print("=" * 50)
    print("对对子模型（输入上联，Ctrl+C 退出）")
    print("=" * 50)

    while True:
        try:
            src = input("\n上联：").strip()
            if not src:
                continue

            src_ids = tokenizer(src.strip(), add_special_tokens=False)['input_ids']
            src_ids = torch.tensor(src_ids, dtype=torch.long)
            print(src_ids, tokenizer.decode(src_ids))


            tgt_ids = model.generate(
                encoder_input_ids=src_ids.to(device),
                max_gen_len=max_model_len,
                decoder_start_token_id=decoder_start_token_id,
                decoder_end_token_id=decoder_end_token_id,
            )
            print(tgt_ids)
            # ===== decode =====
            output_text = tokenizer.decode(tgt_ids)
            print("下联：", output_text)

        except KeyboardInterrupt:
            print("\nBye 👋")
            break

if __name__ == "__main__":
    interactive_chat()

