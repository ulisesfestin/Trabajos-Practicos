
def consecutive(nums, a, b):
    if a in nums and b in nums:
        if (nums.index(a) - nums.index(b)) == 1 or (nums.index(a) - nums.index(b)) == -1:
            return True
        else:
            return False
    else:
        return False

