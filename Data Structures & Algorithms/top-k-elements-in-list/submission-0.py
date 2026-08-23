class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        group=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        for item in items[:k]:
            group.append(item[0])
        return group