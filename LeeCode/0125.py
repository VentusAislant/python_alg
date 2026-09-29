class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        双向指针判断
        """
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1

            while not s[j].isalnum() and j > i:
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

if __name__ == '__main__':
    cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]
    solution = Solution()
    for s, answer in cases:
        my_answer = solution.isPalindrome(s)
        print(my_answer, answer)

