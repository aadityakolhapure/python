def check(s1,s2):
    if(s2.count(s1)>0):
        print("Yes")
    else:
        print("No")
        
s2="Dnyanshree Institute of Engineering and Technology"
s1=input("Enter the string you want to find : ")            
check(s1,s2)