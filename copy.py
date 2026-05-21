import copy
spam = [1,2,3]
eggs = copy.copy(spam) #creates duplicate copy of the list
eggs[1] = 10
print(spam) # [1,2,3]
print(eggs) # [1,10,3]
#######
spam = [1,2,3]
eggs = spam
eggs[1] = 10
print(spam) # [1,10,3]
print(eggs) # [1,10,3]
