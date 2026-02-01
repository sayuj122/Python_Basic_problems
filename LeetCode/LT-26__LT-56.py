# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:]=sorted(set(nums))
        return len(nums)
    
# 58.Length of Last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip().split()
        return len(s[-1])
        