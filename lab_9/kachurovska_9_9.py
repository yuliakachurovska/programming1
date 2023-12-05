n = int(input())
all_votes = []

for i in range(n):
    number_of_votes = int(input())
    votes = []

    for el in range(number_of_votes):
        counter = int(input())
        votes.append(counter)

    all_votes.append(votes)

for k in range(n):
    vote_dict = {}
    for vote in all_votes[k]:
        if vote in vote_dict:
            vote_dict[vote] += 1
        else:
            vote_dict[vote] = 1

    max_count = max(vote_dict.values())
    max_keys = [key for key, value in vote_dict.items() if value == max_count]     # <== будемо чесними, ось це нагуглила :) А все інше сама, чесно-чесно

    min_max_key = min(max_keys)  # найменше значення серед максимальних ключів
    print(min_max_key)