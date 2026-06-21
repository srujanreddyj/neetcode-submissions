class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # left_prod = [1] * len(nums)
        answer = [1] * len(nums)
        right_prod = [1] * len(nums)
        left = 1

        for i in range(len(nums)):
            # left_prod[i] = left_prod[i-1] * nums[i-1]
            answer[i] = left
            left *= nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            right_prod[i] = right_prod[i+1] * nums[i+1]

        for i in range(len(nums)):
            # answer[i] = left_prod[i] * right_prod[i]
            answer[i] = answer[i] * right_prod[i]

        return answer