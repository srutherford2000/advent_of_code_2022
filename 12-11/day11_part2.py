import math
list_of_monkeys = []

the_lcm = 1

class Monkey:
    def __init__(self, current_items, change_func_type, change_func_amount,
                 divisible_int, if_true, if_false):
        self.items = current_items
        self.change_funct_type = change_func_type
        self.change_func_amount = change_func_amount
        self.divisible_int = divisible_int
        self.if_true_monkey = if_true
        self.if_false_monkey = if_false
        self.numbers_seen = 0

    def __repr__(self):
        the_items = ""
        for i in self.items:
            the_items += str(i)+" "
        return "Monkey("+the_items+","+self.change_funct_type + "," + str(self.change_func_amount) + "," + str(self.divisible_int) + "," + str(self.if_true_monkey) + "," + str(self.if_false_monkey) + ")"

    def update_all(self):
        if self.change_funct_type == "*":
            updated_items = []
            for item in self.items:
                if self.change_func_amount == "old":
                    change_func_amount = item
                else:
                    change_func_amount = int(float(self.change_func_amount))
                new_item_val = int(item * change_func_amount )% the_lcm
                updated_items.append(new_item_val)
            self.items = updated_items
            
        elif self.change_funct_type == "/":
            updated_items = []
            for item in self.items:
                if self.change_func_amount == "old":
                    change_func_amount = item
                else:
                    change_func_amount = int(float(self.change_func_amount))
                new_item_val = int(item / change_func_amount ) % the_lcm
                updated_items.append(new_item_val)
            self.items = updated_items

        elif self.change_funct_type == "+":
            updated_items = []
            for item in self.items:
                if self.change_func_amount == "old":
                    change_func_amount = item
                else:
                    change_func_amount = int(float(self.change_func_amount))
                new_item_val = int(item + change_func_amount ) % the_lcm
                updated_items.append(new_item_val)
            self.items = updated_items

        elif self.change_funct_type == "-":
            updated_items = []
            for item in self.items:
                if self.change_func_amount == "old":
                    change_func_amount = item
                else:
                    change_func_amount = int(float(self.change_func_amount))
                new_item_val = int(item - change_func_amount ) % the_lcm
                updated_items.append(new_item_val)
            self.items = updated_items

        else:
            print("this is bad")
            exit()

    def throw_items(self):
        for i in range(len(self.items)):
            this_item = self.items.pop(0)
            if this_item % self.divisible_int == 0:
                list_of_monkeys[self.if_true_monkey].items.append(this_item)
            else:
                list_of_monkeys[self.if_false_monkey].items.append(this_item)

def get_list_no_commas(lists):
    list_of_int = []
    for i in lists:
        if "," in i:
            i = i[:-1]
        list_of_int.append(int(float(i)))
    return list_of_int


in_file = open("input.txt","r")

monkey_line = in_file.readline().strip()

while monkey_line != "":
    item_line = in_file.readline().strip().split()
    operation_line = in_file.readline().strip().split()
    test_line = in_file.readline().strip().split()
    true_line = in_file.readline().strip().split()
    false_line = in_file.readline().strip().split()
    null_line = in_file.readline().strip().split()

    items = get_list_no_commas(item_line[2:])
    op_func = operation_line[4]
    op_val = operation_line[5]
    test_val = int(float(test_line[3]))
    the_lcm = math.lcm(test_val, the_lcm)
    true_val = int(float(true_line[5]))
    false_val = int(float(false_line[5]))

    list_of_monkeys.append(Monkey(items, op_func, op_val, test_val, true_val, false_val))
    

    monkey_line = in_file.readline().strip()

in_file.close()

#print(the_lcm)

#print(list_of_monkeys)


for each_round in range(10000):
    for monkey in list_of_monkeys:
        #first update the monkey
        monkey.update_all()

        #update the number of items seen
        monkey.numbers_seen += len(monkey.items)
        
        #then let the monkey throw stuff
        monkey.throw_items()

#print(list_of_monkeys)

monkey_freq = []

for monkey in list_of_monkeys:
    monkey_freq.append(monkey.numbers_seen)

monkey_freq.sort()

print(monkey_freq[-2] * monkey_freq[-1])
