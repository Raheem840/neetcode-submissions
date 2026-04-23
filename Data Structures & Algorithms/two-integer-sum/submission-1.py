class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_indices = sorted([(val, idx) for idx, val in enumerate(nums)])
        i = 0
        j = len(nums)-1
        result = []
        while i < j:
            current_sum = nums_with_indices[i][0] + nums_with_indices[j][0]
            if current_sum > target:
                j -= 1
            elif current_sum < target:
                i += 1
            elif current_sum == target:
                result.append(min(nums_with_indices[i][1], nums_with_indices[j][1]))
                result.append(max(nums_with_indices[i][1], nums_with_indices[j][1]))
                break

        return result