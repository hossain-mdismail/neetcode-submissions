class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}   # an empty dictionary -> {num: index}

        for i in range(len(nums)):
            check = nums[i]
            if check in seen:   # if key is in seen, tar mane key hobe value gula
                print(f"Got it! The number {check} is already in nums!")
                return True  
            else: seen[nums[i]] = i
        return False            

        