import os
import csv
election_data_csv = os.path.join('Resources', 'election_data.csv')
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Total vote
    total_vote = 0
    candidate_list = []
    for row in csvreader:
        total_vote = total_vote + 1
        candidate_list.append(row[2])
    # List of candidates
    print(f"Total Votes: {total_vote}")
    candidate = []
    for c in candidate_list:
        if c not in candidate:
            candidate.append(c)
    # Votes of each candidate
    candidate_vote_dict = {}
    for v in candidate_list:
        if v in candidate_vote_dict:
            candidate_vote_dict[v] = candidate_vote_dict[v] + 1
        else:
            candidate_vote_dict[v] = 1
    for c in candidate_vote_dict:
        print(
            f"{c}: {round(candidate_vote_dict[c]*100/total_vote,2)}% ({candidate_vote_dict[c]})")
    # Winner
    max_vote = 0
    winner = ""
    for v in candidate_vote_dict:
        if candidate_vote_dict[v] > max_vote:
            max_vote = candidate_vote_dict[v]
            winner = v

        else:
            max_vote = max_vote
            winner = winner
    print(f"Winner: {winner}")
# Export to text
output_path = os.path.join("Analysis", "pypoll_result.txt")

with open(output_path, 'w') as txt:
    txt.write("Election Results: \n")
    txt.write(f"-------------------------- \n")
    txt.write(f"Total Votes : {total_vote} \n")
    txt.write(f"-------------------------- \n")
    for c in candidate_vote_dict:
        txt.write(
            f"{c}: {round(candidate_vote_dict[c]*100/total_vote,2)}% ({candidate_vote_dict[c]})\n")
    txt.write(f"-------------------------- \n")
    txt.write(f"Winner: {winner}")

#  # 2nd candidate
#    txt.write(
#        f"{c}: {round(candidate_vote_dict[c]*100/total_vote,2)}% ({candidate_vote_dict[c]})\n")
    # 3rd candidate
 #   txt.write(
 #       f"{c}: {round(candidate_vote_dict[c]*100/total_vote,2)}% ({candidate_vote_dict[c]})\n")
