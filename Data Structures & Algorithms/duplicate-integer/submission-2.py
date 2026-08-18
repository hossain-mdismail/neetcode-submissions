class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen={}   # an empty dictionary -> {num: index}

        for i in range(len(nums)): # walk through index: 0 to n
            check = nums[i]
            if check in seen:   # if key is in seen, tar mane key hobe value gula
                print(f"Got it! The number {check} is already in nums!")
                return True  # 'return' doesn't care if the loop wanted to keep going.
            else: seen[nums[i]] = i # stoting as {num: index,...}
        return False     # return will immediately eject the function with output       

        