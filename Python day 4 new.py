def datatypes():
    a=int(input("Enter an integer"))
    b=float(input("Enter a floating point number"))
    c=input("Enter a character")
    d=input("Enter a String")
    e1=[]
    for i in range(5):
       e1.append(int(input(f"Enter the element {i+1}")))
    f1=(34,32,55,64,88)
    print(f1)
    g1={1,2,3}
    print(g1)
    g={"Name":"Bhavani","Clg":"PSGCT","Place":"Coimbatore"}
    print("DIFFERENT TYPES OF DATA TYPES AVAILABLE IN PYTHON")
    print("Integer",a)
    print("Float",b)
    print("Character",c)
    print("String",d)
    print("List",e1)
    print("Tuple",f1)
    print("Dictionary",g)
    print("Set",g1)
def getlist():
    l=[1,2,4,5,"Bhav","PSG",[1,2,3],(2,5)]
    for i in range(len(l)):
        print(f"Element {i+1} is {l[i]}")
def get():
    p=int(input("Enter the first number:"))
    q=int(input("Enter the second number:"))
    h=[]
    h.extend([p,q])
    print(h)
    for i in h:
        print(i)
datatypes()
getlist()
get() 
