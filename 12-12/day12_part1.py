in_file = open("input.txt","r")

import sys
sys.setrecursionlimit(10**6)


letter_map = {}
letter_map["S"]=0
letter_map["E"]=25
lets = "abcdefghijklmnopqrstuvwxyz"
for i in range(26):
    letter_map[lets[i]] = i

grid = []
min_path = []

end_col = 0
end_row = 0

start_col = 0
start_row = 0


row = 0

for line in in_file:
    line = line.strip()
    split_line = list(line)
    grid.append(split_line)
    min_path.append(len(split_line)*[-99])
    if "E" in split_line:
        end_col = split_line.index("E")
        end_row = row
    if "S" in split_line:
        start_col = split_line.index("S")
        start_row = row
    row += 1

in_file.close()

def find_valid_next_nodes(this_row, this_col):
    possible_next_paths = [[this_row+1,this_col],[this_row-1,this_col],[this_row,this_col+1],[this_row,this_col-1]]
    valid_next_paths = []
    for [possible_row, possible_col] in possible_next_paths:
        if ((possible_row >= len(grid)) or (possible_row <0) or
            (possible_col >= len(grid[0])) or (possible_col <0)):
            pass
        else:
            if (( letter_map[grid[possible_row][possible_col]] - letter_map[grid[this_row][this_col]]) <=1):
                valid_next_paths.append((possible_row,possible_col))    
    return valid_next_paths



seen = {}
my_fake_queue = [] #holds a [current row pos, current col pos, path length, visited nodes
my_fake_queue.append([start_row, start_col, 0])

found_end_node = False

while (found_end_node == False) and (len(my_fake_queue)>0):
    [a_row,a_col,path_len] = my_fake_queue.pop(0)
    if (a_row == end_row) and (a_col == end_col):
        found_end_node = True
        print(path_len)
    else:
        possible_next_elements = find_valid_next_nodes(a_row,a_col)
        new_len = path_len+1
        for (next_pos) in possible_next_elements:
            if (next_pos not in seen) or (seen[next_pos] > new_len):
                my_fake_queue.append([next_pos[0], next_pos[1], new_len])
                seen[next_pos] = new_len
        


