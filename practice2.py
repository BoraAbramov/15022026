

'''
Exercise 1: The "Guest List" Cleaner
You have a list of names for a party, but some people signed up twice.
- Create a list called guests with these values: "Alice", "Bob", "Charlie", "Alice", "David", "Bob"
- Use a set to automatically remove the duplicates
- Check if "Emma" is in your set. If she is not there, add her
- Print the final number of unique guests using len()

Exercise 2: Safe Deletion Race
- Create a set called codes containing: 101, 102, 103, 104
- Use .pop() to remove one random code and print it
- Try to use .remove() to delete the number 999 --> ERROR!, so- Wrap it with if to avoid crash
- Use .discard() to delete the number 999
'''

_gusts = ["Alice", "Bob", "Charlie", "Alice", "David", "Bob"]
_gusts_set = set(_gusts)

if "Emma" not in _gusts_set:
    _gusts_set.add("Emma")

print(len(_gusts_set))

nums = {101, 102, 103, 104}

print(nums.pop())

if 999 in nums:
    nums.remove(999)

nums.discard(999)
print(nums)

# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
# **BONUS**
import random

random_nums = []

for i in range(30):
    num = random.randint(1, 10)
    random_nums.append(num)

print(random_nums)

# print each number and how many times, without duplications
# hint: sort, set, count
# [1, 4, 2, 2, 1, 5]
# 1: 2-times
# 2: 2-times
# 4: 1-time
# 5: 1-time

for item in sorted(random_nums):
    while item != i:
        i = item
        print(f"the number {item} appears {random_nums.count(item)} times")

print("-" * 50)

_sederole = []
_mispar = []

for item in sorted(random_nums):
    while item != i:
        i = item
    if random_nums.count(item) > len(random_nums):
        _sederole.append(item)
        _mispar.append(_oreh)
    elif random_nums.count(item) < _oreh:
        _sederole.insert(item)
        _mispar.append(_oreh)

