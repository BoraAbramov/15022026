
votes = []

while True:
    votes.append(input("Please enter your ID: "))
    if votes[-1] == "" or votes[-1].isalpha():
        votes.pop()
        continue
    votes[-1] = int(votes[-1])
    if votes[-1] == -999:
        votes.pop()
        break
    if votes[-1] < 0 or votes[-1] > 100:
        votes.pop()

#print(votes)

votes_copy = votes.copy() #original list backup
votes_set = set(votes)
invalid_voters = set()
_appear = len(votes)

for item in votes:
    if votes.count(item) > 1:
        invalid_voters.add(item)

for item in invalid_voters:
    while item in votes:
        votes.remove(item)

invalid_voters = list(invalid_voters)
votes_set = list(votes)

print(f"invalid voters {sorted(invalid_voters)}") #good
print(f"valid voters {sorted(votes)}")
print(f"vote attempts {_appear}")

