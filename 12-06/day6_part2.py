in_file = open("input.txt","r")
number_unique = 14

the_lines = in_file.readline()

in_file.close()

for i in range(number_unique,len(the_lines)):
    this_subset = list(the_lines[i-number_unique:i])
    if len(set(this_subset)) == number_unique:
        print(i)
        break

  
