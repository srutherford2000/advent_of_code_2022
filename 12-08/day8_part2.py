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
            return row-r
    return row

def hidden_down(col, row):
    for r in range(row+1, HEIGHT):
        if tree_grid[r][col] >= tree_grid[row][col]:
            return r-row
    return HEIGHT-1-row

def hidden_left(col, row):
    for c in range(col-1, -1, -1):
        if tree_grid[row][c] >= tree_grid[row][col]:
            return col-c
    return col

def hidden_right(col, row):
    for c in range(col+1,WIDTH):
        if tree_grid[row][c] >= tree_grid[row][col]:
            return c-col
    return WIDTH-1-col

max_forest_score = 0

for h in range(1,HEIGHT-1):
    for w in range(1,WIDTH-1):
        up_score = hidden_up(w,h)
        down_score = hidden_down(w,h)
        left_score = hidden_left(w,h)
        right_score = hidden_right(w,h)
        this_forest_score = up_score * down_score * left_score*right_score
        #print(tree_grid[h][w],h,w,this_forest_score,up_score, down_score, left_score, right_score)
        max_forest_score = max([this_forest_score, max_forest_score])

print(max_forest_score)
        
