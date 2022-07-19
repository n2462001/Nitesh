#13
def grouping_dictionary(l):
    result={}
    for k,v in l:
        result.setdefault(k,[]).append(v)
    return result
colors=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
print("Original list :")
print(colors)
print("\n Grouping a sequence of key value pair:")
print(grouping_dictionary(colors))
print()
#14
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result
student_section = ["Yashan", "Sumit", "Yuvraj", "choori"]
student_name = ["C2", "C1", "C2", "C3"]
student_marks = [85,98,89,92]
print("Original strings:")
print(student_section)
print(student_name)
print(student_marks)
print("\nNested dictionary:")
print(nested_dictionary(student_section, student_name, student_marks))
print()
#15
print("To check if a set is subset of another set:")
def check_subset(s,S):
    if(s.issubset(S)):
        print(s ,"is a subset of ", S)
    else:
        print(s ,"is not a subset of ", S)
a={1,5,16,56}
print(a)
b={1,5,16,56,85}
print(b)
check_subset(a,b)
print()
#16
print("To create symmetric difference & set difference:")
A={15,21,5,87}
print(A)
B={15,21,55,87}
print(B)
print("Symmetric difference of A and B is ",A.symmetric_difference(B))
print("Symmetric difference of B and A is ",B.symmetric_difference(A))
print("Set difference of A and B is ",A.difference(B))
print("Set difference of B and A is ",B.difference(A))
print()
#17
print("To remove a empty tuple from list of tuples:")
def Remove(tuples):
    tuples=[t for t in tuples if t]
    return tuples
tuples=[('Sumit'),(),('yash'),('suhszz'),()]
print(Remove(tuples))
print()
#19
print("To check validity of password:")
l, u , d , s = 0 , 0 , 0 , 0
Password = 'Yashanpal6^'
lowercasealphabets='asdfghjklpoiuytrewqzxcvbnm'
uppercasealphabets='ASDFGHJKLPOIUYTREWQZXCVBNM'
digits="0123456789"
specialchar='!@#$%^&*'
if (len(Password) >= 8):
    for i in Password:
        if (i in lowercasealphabets):
            l+=1
        if (i in uppercasealphabets):
            u+=1    
        if (i in digits):
            d+=1    
        if (i in specialchar):
            s+=1
if (l>=1 and u>=1 and d>=1 and s>=1 and l+u+d+s==len(Password)):
    print("Password is valid")   
else:
    print("Password is  not valid")
