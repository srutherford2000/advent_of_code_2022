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

point_to_tool ={}
point_to_tool["Rock"] = 1
point_to_tool["Paper"] = 2
point_to_tool["Scissors"]=3

def new_strat(p1,p2):
    #returns p2 score
    if p2 =="X":
        if player1_map[p1] == "Rock": #we lost to rock with scissors
            return point_to_tool["Scissors"]
        elif player1_map[p1] == "Paper": #we lost to paper with rock
            return point_to_tool["Rock"]
        else: #we lost to scisors with paper
            return point_to_tool["Paper"]
    elif p2 == "Y":
        score = 3 #we draw
        score += point_to_tool[player1_map[p1]]
        return score
    else:
        score = 6 #we win
        if player1_map[p1] == "Rock": #we won to rock with paper
            return score + point_to_tool["Paper"]
        elif player1_map[p1] == "Paper": #we won to paper with scissors
            return score + point_to_tool["Scissors"]
        else: #we won to scissors with rock
            return score + point_to_tool["Rock"]

        
p2_score = 0

for [this_p1,this_p2] in rounds:
    p2_score_this_round = new_strat(this_p1,this_p2)
    p2_score+=p2_score_this_round

print("P2:",p2_score)
    
