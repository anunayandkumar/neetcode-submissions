class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans= []

        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        count = count.items()
        count = sorted(count, key = lambda x: x[1], reverse = True)
        count = list(count)
        for i in range(k):
            ans.append(count[i][0])
        




        return ans
                

        

        