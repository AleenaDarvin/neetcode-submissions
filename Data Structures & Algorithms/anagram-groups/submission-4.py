class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        visited=[False]*len(strs)
        for i in range(len(strs)):
            if visited[i]:
                continue
            word=[strs[i]]
            visited[i]=True
            for j in range(i,len(strs)):
                if not visited[j] and sorted(strs[i])==sorted(strs[j]):
                        word.append(strs[j])
                        visited[j]=True
            ans.append(word)
        return ans

                
        