in_file = open("input.txt","r")

register_val_at_cycle = [1]
i = 0


for line in in_file:
    line = line.strip()
    split_line = line.split()
    if len(split_line) == 1: #it was a noop
        register_val_at_cycle.append(register_val_at_cycle[i])
        i+=1
    elif len(split_line) == 2: #its a addx
        the_num = int(float(split_line[1]))     
        register_val_at_cycle.append(register_val_at_cycle[i])
        i+=1
        register_val_at_cycle.append(register_val_at_cycle[i] + the_num)
        i+=1
    else:
        print("we shoudln't be here")
        exit()

in_file.close()


cycle = 19

ans = 0

for i in range(cycle,len(register_val_at_cycle),40):
    #print(register_val_at_cycle[i], i+1, register_val_at_cycle[i]*(i+1))
    ans += register_val_at_cycle[i]*(i+1)

#print()
print(ans)
