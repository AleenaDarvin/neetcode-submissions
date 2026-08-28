class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=left
        count=0
        st=set()
        while right<len(s):
            if s[right] not in st:
                st.add(s[right])
                right+=1
                count=max(count,right-left)
            else:
                st.remove(s[left])
                left+=1
        return count
        