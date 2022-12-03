import string
in_file = open("input.txt","r")

alphabet = [0] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

ruck_sacks = []

for line in in_file:
    line = line.strip()
    ruck_sacks.append(line)
in_file.close()


total_sum = 0

for i in range(0,len(ruck_sacks),3):
    ruck1=ruck_sacks[i]
    ruck2=ruck_sacks[i+1]
    ruck3=ruck_sacks[i+2]
  
    for let in ruck1:
        if let in ruck2:
            if let in ruck3:
                let_num_val = alphabet.index(let)
                total_sum += let_num_val
                break

print(total_sum)
            
