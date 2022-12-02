in_file = open("input.txt","r")

rounds = []

for line in in_file:
    line = line.strip()
    rounds.append(line.split())

in_file.close()

player1_map = {}
player1_map["A"]="Rock"
player1_map["B"]="Paper"
player1_map["C"]="Scissors"

player2_map = {}
player2_map["X"]="Rock"
player2_map["Y"]="Paper"
player2_map["Z"]="Scissors"

point_to_tool ={}
point_to_tool["Rock"] = 1
point_to_tool["Paper"] = 2
point_to_tool["Scissors"]=3

def who_won(p1,p2):
    if player1_map[p1] == player2_map[p2]:
        return [3,3]
    if player1_map[p1] == "Rock":
        if player2_map[p2] == "Paper":
            return [0,6]
        else: #player2 did scissors
            return [6,0]
    elif player1_map[p1] == "Paper":
        if player2_map[p2] == "Rock":
            return [6,0]
        else: #player2 did scissors
            return [0,6]
    elif player1_map[p1] == "Scissors":
        if player2_map[p2] == "Paper":
            return [6,0]
        else: #player2 did rock
            return [0,6]

p1_score = 0
p2_score = 0

for [this_p1,this_p2] in rounds:
    [p1_score_pt1, p2_score_pt1] = who_won(this_p1, this_p2)
    p1_score_pt2 = point_to_tool[player1_map[this_p1]]
    p2_score_pt2 = point_to_tool[player2_map[this_p2]]

    p1_score_this_round = p1_score_pt1+p1_score_pt2
    p2_score_this_round = p2_score_pt1+p2_score_pt2

    p1_score += p1_score_this_round
    p2_score += p2_score_this_round

print("P1:",p1_score)
print("P2:",p2_score)
    
