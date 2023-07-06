# union with repetition
list1 = [1,2,3,4,5,6]
print("First list is:",list1)
list2 = [2,4,6,8,10,12]
print("Second list is:",list2)
newList=[]
newList.extend(list1)
for element in list2:
    # for union without repetition
    # if element not in list1
    newList.append(element)
print("Union of the list is:",newList)    
