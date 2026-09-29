class Solution:
    def reverseWords(self, s: str) -> str:
        """
        时间复杂度 O(N), 空间复杂度 O(N)
        """
        return " ".join(reversed(s.strip().split()))


if __name__ == '__main__':
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a")
    ]
    s = Solution()

    for (input, answer) in test_cases:
        my_answer = s.reverseWords(input)
        print(my_answer, " | ",  answer)
