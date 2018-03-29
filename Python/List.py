my_list = []
Str = "If President Trump actually meets Kim Jong-un in the next few months "
for i in range(len(Str)):
    my_list.append(Str[i])
# print(my_list)
list = []
words = " [ an encounter that many American officials still doubt will come to pass ]"
for item in range(len(words)):
    my_list.extend(words[item])
print(" \n \n ")
my_list.insert(0, "OMER GAD")  # insert to  index
my_list.remove("I")  # bu elamen silmek icin
for indes in range(24):
    my_list.pop()
# my_list.clear()
print(my_list)
print("\n")
print(my_list.index("r"))
print(my_list.count("l"))
my_list.reverse()
print("\n   \n ")
print(my_list)
