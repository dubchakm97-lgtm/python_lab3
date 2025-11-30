class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        length = len(nums)
        while True:
            count = 0
            for spin in range(1, length):
                if nums[spin] < nums[spin - 1]:
                    nums[spin], nums[spin - 1] = nums[spin - 1], nums[spin]
                    count += 1
            if count == 0:
                break
        return nums[-k]
