in_file = open("input.txt")

cal_list = []
cur_cal = 0

for line in in_file:
    line = line.strip()
    if line != "":
        cur_cal += int(float(line))

    else:
        cal_list.append(cur_cal)
        cur_cal = 0

cal_list.append(cur_cal)


in_file.close()

cal_list.sort()
cal_list.reverse()

top_3 = sum(cal_list[:3])

print("most calories:",top_3)        
