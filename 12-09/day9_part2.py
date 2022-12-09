in_file = open("input.txt")

directions = []

for line in in_file:
    line=line.strip()
    line_split = line.split()
    directions.append(line_split)

in_file.close()

the_ropes = {}

for i in range(10):
    the_ropes[i] = [0,0]

visited_t_pos = set()
visited_t_pos.add(tuple(the_ropes[9]))

direction_map = {}
direction_map["R"] = [0,1]
direction_map["L"] = [0,-1]
direction_map["U"] = [1,0]
direction_map["D"] = [-1,0]
direction_map["UR"] = [1,1]
direction_map["UL"] = [1,-1]
direction_map["DR"] = [-1,1]
direction_map["DL"] = [-1,-1]



def h_t_touching(h_x, h_y, t_x, t_y):
    dist = (t_x-h_x)**2 + (t_y-h_y)**2
    if dist <=2:
        return True
    else:
        return False
    
def sum_two_lists(lt1, lt2):
#CREDIT TO https://www.javatpoint.com/how-to-add-two-lists-in-python#:~:text=The%20sum()%20function%20is,elements%20using%20index%2Dwise%20lists.
#for the equation to sum two lists
    result_lt = [sum(i) for i in zip(lt1, lt2 )]
    return result_lt

def update_t(h_x, h_y, t_x, t_y):
    how_to_move = None
    if h_x == t_x: #were in the same row
        if h_y > t_y: #h_y is 2 or more steps above t_y, so move t_y up
            how_to_move = direction_map["U"]
        else: #h_y is 2 or more steps belo t_y, move t_y down
            how_to_move = direction_map["D"]
    elif h_y == t_y: #were in the same row
        if h_x > t_x:#h_x is 2 or more steps to the right of t_x, move t_x right
            how_to_move = direction_map["R"]
        else: #h_x is 2 or more steps to the left of t_x, move t_x to the left
            how_to_move = direction_map["L"]
    else: # we are some diagnoal away
        the_code = ""
        if h_y > t_y:
            the_code += "U"
        else:
            the_code += "D"
        if h_x> t_x:
            the_code += "R"
        else:
            the_code += "L"
        how_to_move = direction_map[the_code]
    
    return sum_two_lists([t_y, t_x], how_to_move)


for [direction, dist] in directions:
    dir_update = direction_map[direction]
    #print("MOVE", direction, dist)
    for each_step in range(int(float(dist))):
        the_ropes[0] = sum_two_lists(the_ropes[0], dir_update)

        for i in range(1,10):
            touching = h_t_touching(the_ropes[i-1][1], the_ropes[i-1][0], the_ropes[i][1], the_ropes[i][0])
            #print("touching?", touching)
            if touching == False:
                the_ropes[i] = update_t(the_ropes[i-1][1], the_ropes[i-1][0], the_ropes[i][1], the_ropes[i][0])

            if i ==9:
                visited_t_pos.add(tuple(the_ropes[9]))
            #print("h_pos",the_ropes[i-1])
            #print("t_pos",the_ropes[i])
    #print()
print(len(visited_t_pos))
            
    
    
