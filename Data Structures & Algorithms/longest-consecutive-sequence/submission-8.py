class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arr=[]
        hset=set()
        items=sorted(nums)
        for i in items:
            hset.add(i)
        arr=sorted(list(hset))
        if len(arr)==0:
            return 0
        else:
            longest=1
            current=1
        for i in range(len(arr)-1):
            diff=abs(arr[i+1]-arr[i])
            if diff==1:
                current+=1
            else:
                longest=max(longest,current)
                current=1
        longest=max(longest,current)
        return longest
            
        

        