class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr= []
        p = 1
        count_zero = 0

        for i in nums:
            p *= i
            if i==0:
                count_zero += 1
        if count_zero>1:
            return [0] * len(nums)
        elif count_zero==1:
            ans = []
            index = i
            product = 1
            for i in range(len(nums)):
                if nums[i] == 0:
                    index = i
                    break
            i = 0
            while(i<len(nums)):
                if i!=index:
                    product *= nums[i]
                i += 1
            ans = [0] * len(nums)
            ans[index] = product
            return ans


        else:    
            for i in range(len(nums)):
                arr.append(p//nums[i])
            return arr
        