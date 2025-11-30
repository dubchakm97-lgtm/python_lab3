class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        lst = []
        new_list = [0 for x in range(0, max(nums) + 1)]
        for element in nums:
            new_list[element] += 1
        while k != 0:
            for _ in new_list:
                if _ == max(new_list):
                    lst.append(new_list.index(_))
                    k -= 1
                    new_list[new_list.index(_)] = 0
                    break
        return lst
