import random
nums = []

for i in range(10):
    i = random.randint(1,100)
    nums.append(i)
print(nums)

for i in range(0, len(nums)-1, 2):
    nums[i], nums[i+1] = nums[i+1], nums[i]

print(nums)