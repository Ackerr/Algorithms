from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = [0] + nums
        for i in range(1, len(nums) + 1):
            self.nums[i] = self.nums[i] + self.nums[i - 1]

    def sum_range(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]
