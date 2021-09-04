f = open("herding.in", "r")
g = open("herding.out", "w")

def checkDone(nums):
   if len(nums) < 1:
      return False
   min_val = min(nums)
   max_val = max(nums)
   if max_val - min_val + 1 == len(nums):
      for i in range(len(nums)):
         if nums[i] < 0:
            j = -nums[i] - min_val
         else:
            j = nums[i] - min_val
            if nums[j] > 0:
               nums[j] = -nums[j]
            else:
               return False
      return True
   return False

cows = f.readline().split(" ")
print(cows)