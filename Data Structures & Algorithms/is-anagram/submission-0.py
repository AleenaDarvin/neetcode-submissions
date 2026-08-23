class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1=s
        word2=t
        if sorted(s)==sorted(t):
            return True
        else:
            return False
        