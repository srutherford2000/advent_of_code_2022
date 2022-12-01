in_file = open("input.txt")

max_cal = 0
cur_cal = 0

for line in in_file:
    line = line.strip()
    if line != "":
        cur_cal += int(float(line))

    else:
        if cur_cal > max_cal:
            max_cal = cur_cal
        cur_cal = 0

if cur_cal > max_cal:
    max_cal = cur_cal


in_file.close()

print("most calories:",max_cal)        
