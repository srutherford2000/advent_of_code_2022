in_file = open("input.txt","r")



class File:
    def __init__(self, f_name, size):
        self.name = f_name
        self.size = int(float(size))

        
    def __repr__(self):
       return "File("+self.name+")"

class Directory:
    def __init__(self, parent, dir_name):
        self.parent = parent
        self.name = dir_name
        self.files = []
        self.sub_directories = []

    def __repr__(self):
        list_of_files = ""
        for file in self.files:
            list_of_files+= repr(file) +" "
        list_of_dirs = ""
        for direct in self.sub_directories:
            list_of_dirs+= repr(direct) +" "
        return "Directory("+self.name+" , "+list_of_files+", "+list_of_dirs+")"

    def size_of_dir(self):
        total_size = 0
        for file in self.files:
            total_size += file.size
        for each_dir in self.sub_directories:
            total_size += each_dir.size_of_dir()
        return total_size

        
start_dir = Directory("/", "/")
working_dir = start_dir


line = in_file.readline().strip()

while line != None:
    split_line = line.split()

    if "cd"in split_line: #move back a directory
        if ".." in split_line:
            if working_dir.parent != None:
                working_dir = working_dir.parent
        else:
            the_dir_to_move_into = line.split()[2]
            if "/" == the_dir_to_move_into:
                working_dir = start_dir
            else:
                for directory in working_dir.sub_directories:
                    if directory.name == the_dir_to_move_into:
                        working_dir = directory
            
    elif "ls" in split_line:
        pass
    elif "dir" in split_line:        
        dir_name = line.split()[1]
        new_dir = Directory(working_dir, dir_name)
        working_dir.sub_directories.append(new_dir)
    else: #this is a file
        file_size, file_name = line.split()
        new_file = File(file_name, file_size)
        working_dir.files.append(new_file)
    


    line = in_file.readline().strip()
    if line == "":
        line = None


in_file.close()

def get_all_sub_sizes (a_dir):
    all_dirs = [a_dir.size_of_dir()]
    for each_dir in a_dir.sub_directories:
        all_dirs += get_all_sub_sizes(each_dir)
    return all_dirs

list_of_subdirectories_size = get_all_sub_sizes(start_dir)

sub_directories_smaller_100000_sum = 0

for dir_size in list_of_subdirectories_size:
    if dir_size <= 100000:
        sub_directories_smaller_100000_sum += dir_size

#print(list_of_subdirectories_size)
print(sub_directories_smaller_100000_sum)
