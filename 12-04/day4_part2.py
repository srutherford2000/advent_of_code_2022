in_file = open("input.txt","r")

data = []

def list_str_to_list_int(the_list):
    a = []
    for stringy in the_list:
        a.append(int(float(stringy)))
    return a

for line in in_file:
    line = line.strip()
    split_up = line.split(",")
    split_split_up = (list_str_to_list_int(split_up[0].split("-")),
                      list_str_to_list_int(split_up[1].split("-")))
    data.append(split_split_up)

in_file.close()

num_contained = 0

for (elf1,elf2) in data:
    if elf1[0] < elf2[0]:
        smaller_elf = elf1
        bigger_elf = elf2
    else:
        smaller_elf = elf2
        bigger_elf = elf1
    if smaller_elf[0] == bigger_elf[0] or bigger_elf[0] <= smaller_elf[1]:
        num_contained += 1
        
print(num_contained)

        
        
        
        
