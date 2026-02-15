'''
Do:
Print nums sorted ascending (without changing original)
Sort nums in-place descending
Print words alphabetically A→Z
Print words by length shortest→longest
Print words by length longest→shortest. hint: reverse=True
'''

nums = [7, 1, 9, 2, 2, 10]
words = ["banana", "kiwi", "apple", "fig", "watermelon"]

print(sorted(nums))

nums.sort(reverse=True)
print(nums)

print(sorted(words))

print(sorted(words, key=len))

print(sorted(words, key=len, reverse=True))

print(nums[::2])

