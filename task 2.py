
votes = []

while True:
    votes.append(input("Please enter your ID: "))
    votes[-1] = int(votes[-1])
    if votes[-1] == -999:
        votes.pop()
        break
    if votes[-1] < 0 or votes[-1] > 100:
        votes.pop()

print(votes)

votes_copy = votes.copy()
votes_set = {}
invalid_voters = {}
_attemps = len(votes)

for item in votes:
    if votes.count(item) > 1:
        invalid_voters.add(item)
        votes.pop(item)

