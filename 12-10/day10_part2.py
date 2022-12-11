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


crt_display = ""

for cycle, reg_val in enumerate(register_val_at_cycle):
    mod_cycle = cycle %40
    if mod_cycle == 0:
        crt_display += "\n"

    if reg_val== max(0,mod_cycle-1) or reg_val==mod_cycle or reg_val==min(39, mod_cycle+1):
        crt_display += "#"
    else:
        crt_display += "."

print(crt_display)
