class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=0
        left=0
        profit=0
        right=left+1
        while right<len(prices):
            if prices[left]>=prices[right]:
                left=right
                right=right+1
            else:
                buy=prices[left]
                if buy<prices[right]:
                    sell=prices[right]
                profit=max(profit,sell-buy)
                right+=1
                
        return profit

        