class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        nums = sorted(nums)
        f, s, l = 0, 1, len(nums) - 1
        mem = []
        while f != len(nums) - 2:
            while l > s:
                sum = nums[f] + nums[s] + nums[l]
                if sum == 0:
                    temp = []
                    temp.append(nums[f])
                    temp.append(nums[s])
                    temp.append(nums[l])
                    if temp not in mem:
                        mem.append(temp)
                    s += 1
                    l -= 1
                elif sum > 0:
                    l -= 1
                elif sum < 0:
                    s += 1
            f += 1
            s = f + 1
            l = len(nums) - 1
        return mem


