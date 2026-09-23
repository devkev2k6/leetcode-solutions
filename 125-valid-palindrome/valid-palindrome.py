class Solution:
    def isPalindrome(self, s: str) -> bool:
        f=""
        for n in s:
            if n.isalnum():
                f+=n.lower()
        return (f==f[::-1])

        