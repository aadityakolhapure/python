def RemoveWord(list,word,n):
    newList = []
    count = 0
    
    for i in list:
        if(i == word):
            count =   count + 1
            if(count != n):
                newList.append(i)
        else:
            newList.append(i)

    lst = newList

    if count== 0:
        print("Item not found")
    else:
        print("Update list is: ",list)
    return newList

list = ["sunday","monday","tuesday","monday"]
word = "sunday"
RemoveWord(list,word,4)
  
