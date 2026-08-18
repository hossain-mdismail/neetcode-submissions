class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # it is an empty dictionary where key is nums and value is indexes
        for i in range(len(nums)):  # i is the index of nums here
            
            diff = target - nums[i]
            if diff in seen:
                print(f"matched pair found")
                return [seen[diff],i]
            else: seen[nums[i]] = i 
                
    
