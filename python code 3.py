list1 = ["ammu","swarupa","teja"]
list2 = ["jacks","jay","anith"]
list3 = ["sandhya","devi","hyndavi"]
index_list = ["a","b","c"]
final_list = [list1,list2,list3]

user_input = input("where to ? --")

letter_index = index_list.index(user_input[0])
number_index = int(user_input[1])-1
final_list[number_index][letter_index] = "something"

print(f"{list1}\n{list2}\n{list3}]")