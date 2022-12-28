nums = list(map(int, input().split()))
l = len(nums)
for i in range(0, l if l % 2 == 0 else l - 1,2):
    nums[i], nums[i + 1] = nums[i + 1], nums[i]

print(nums)
