in_file = open("input.txt","r")

def get_list_from_line (line):
    line_split = line.split(" -> ")
    real_output = []
    for part in line_split:
        comma_split = part.split(",")
        this_part = []
        for subpart in comma_split:
            this_part.append(int(float(subpart)))
        real_output.append(this_part)
    return real_output

def write_rock_paths (list_of_movments):
    last_x = None
    last_y = None
    biggest_y = 0

    for (x,y) in line_as_lst:
        #print("item",x,y, last_x, last_y)
        if last_x == None and last_y==None:
            last_x = x
            last_y = y
            points_with_things[(x,y)] = "r" #theres a rock at this location
        else:
            if last_x <= x and last_y <= y:
                for new_x in range(last_x, x+1):
                    for new_y in range(last_y, y+1):
                        points_with_things[(new_x,new_y)] = "r"
                last_x = new_x
                last_y = new_y
            elif last_x <= x:
                for new_x in range(last_x, x+1):
                    for new_y in range(last_y,y-1,-1):
                        points_with_things[(new_x,new_y)] = "r"
                last_x = new_x
                last_y = new_y
            else:
                for new_x in range(last_x, x-1,-1):
                    for new_y in range(last_y, y-1,-1):
                        points_with_things[(new_x,new_y)] = "r"
                last_x = new_x
                last_y = new_y                

        if last_y > biggest_y:
            biggest_y = last_y
    return biggest_y
    

points_with_things = {}
biggest_y = 0

for line in in_file:
    line = line.strip()
    line_as_lst = get_list_from_line(line)
    #print(line_as_lst)
    this_big_y = write_rock_paths(line_as_lst)
    if this_big_y > biggest_y:
        biggest_y = this_big_y


in_file.close()

#print(points_with_things)
#print(biggest_y)

ABBYS_Y = biggest_y

def sand_trickle(cur_x,cur_y):
    next_3_possibilites = [(cur_x, cur_y+1), (cur_x-1,cur_y+1),(cur_x+1,cur_y+1)]
    options = []
    for possibility in next_3_possibilites:
        if possibility in points_with_things:
            pass
        else:
            options.append(possibility)

    if len(options) == 0: #we can't go anywhere
        points_with_things[(cur_x,cur_y)] = "s" #place a sand drop
        return True
    elif cur_y > ABBYS_Y:
        return False
    else:
        keep_falling_from_x,keep_falling_from_y = options.pop(0)
        return sand_trickle(keep_falling_from_x, keep_falling_from_y)
        
drop_sand = sand_trickle(500,0)
num_dropped = 0

while drop_sand:
    num_dropped +=1
    drop_sand = sand_trickle(500,0)
    
print(num_dropped)

            
    
