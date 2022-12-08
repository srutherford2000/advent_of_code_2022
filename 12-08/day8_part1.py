in_file = open("input.txt")

tree_grid = []

for line in in_file:
    line=line.strip()
    split_line = list(line)
    row_of_trees = []
    for each_str_num in split_line:
        row_of_trees.append(int(float(each_str_num)))
    tree_grid.append(row_of_trees)

in_file.close()

WIDTH = len(tree_grid[0])
HEIGHT = len(tree_grid)
          
def hidden_up(col, row):
    for r in range(row-1,-1,-1):
        if tree_grid[r][col] >= tree_grid[row][col]:
            return True
    return False

def hidden_down(col, row):
    for r in range(row+1, HEIGHT):
        if tree_grid[r][col] >= tree_grid[row][col]:
            return True
    return False

def hidden_left(col, row):
    for c in range(col-1,-1,-1):
        if tree_grid[row][c] >= tree_grid[row][col]:
            return True
    return False

def hidden_right(col, row):
    for c in range(col+1,WIDTH):
        if tree_grid[row][c] >= tree_grid[row][col]:
            return True
    return False

num_visible = 2*WIDTH + 2*HEIGHT - 4
#print(num_visible)

for h in range(1,HEIGHT-1):
    for w in range(1,WIDTH-1):
        is_hidden_up = hidden_up(w,h)
        is_hidden_down = hidden_down(w,h)
        is_hidden_right = hidden_right(w,h)
        is_hidden_left = hidden_left(w,h)
        #print(h,w,is_hidden_up, is_hidden_down, is_hidden_left, is_hidden_right)
        if (is_hidden_up==False or
            is_hidden_down==False or
            is_hidden_right==False or
            is_hidden_left==False):
            num_visible += 1

print(num_visible)
        
