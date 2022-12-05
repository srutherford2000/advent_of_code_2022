#STUFF TO EDIT
in_file = open("input.txt","r")
num_col = 9

#STUFF TO LEAVE
at_start = True

#init the lists for each line in a dict
crates_in_col = {}
for num in range(num_col):
    crates_in_col[num] = []

def updates_list_in_crates(the_line):
    the_line = " " + the_line
    n = 0
    the_loc = 2 + n*4
    while the_loc < len(the_line):
        if the_line[the_loc] != " ":
            crates_in_col[n].append(the_line[the_loc])
        n += 1
        the_loc = the_loc = 2 + n*4

#read in the lines
for line in in_file:
    #line = line.strip()
    if "[" in line:
        updates_list_in_crates(line)
    elif "move" in line:
        line = line.strip()
        split_line = line.split()
        how_many_to_move = int(float(split_line[1]))
        src = int(float(split_line[3])) -1 
        dst = int(float(split_line[5]))-1

        the_old_order = []
        for i in range(how_many_to_move):
            the_old_order.append(crates_in_col[src].pop(0))

        crates_in_col[dst] = the_old_order + crates_in_col[dst]



in_file.close()

ans = ""
for i in range(num_col):
    try:
        ans += crates_in_col[i][0]
    except:
        pass

print(ans)
