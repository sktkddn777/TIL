def solution(nums):
    max_pocket = int(len(nums) / 2)
    nums = list(set(nums))
    
    if max_pocket >= len(nums):
        answer = len(nums)
    else:
        answer = max_pocket
    return answer