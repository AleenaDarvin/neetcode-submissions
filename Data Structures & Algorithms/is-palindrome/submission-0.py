class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        result=""
        for ch in s:
            if ch.isalnum():
                result+=ch
        left=0
        right=len(result)-1
        while left<right:
            if result[left]!=result[right]:
                return False
            left+=1
            right-=1
        return True


        
        