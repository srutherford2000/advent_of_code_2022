import string
in_file = open("input.txt","r")

alphabet = [0] + list(string.ascii_lowercase) + list(string.ascii_uppercase)

ruck_sacks = []

for line in in_file:
    line = line.strip()
    half = int(len(line)/2)
    ruck_sacks.append((line[:half],line[half:]))
in_file.close()


total_sum = 0

for (compart1,compart2) in ruck_sacks:
    for let in compart1:
        if let in compart2:
            let_num_val = alphabet.index(let)
            total_sum += let_num_val
            break

print(total_sum)
            
