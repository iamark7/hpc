class MyClass:
    #Default constructor
    def __init__(self,x=0,y=None):
        print("In Init")
        self.num=x
        self.str=y
        
    def __add__(self,other):
        print("In add")
        if(isinstance(other,MyClass)):
           s=self.num+ord(self.str[0])
           p=str(other.num+ord(other.str[0]))
           c=MyClass(s,p)
           return c
        else:
           return  MyClass(self.num+other,str(ord(self.str[0])+other))
    def __radd__(self,other):
        print("In radd")
        return  MyClass(self.num+other,str(ord(self.str[0])+other))
    


           

ob1=MyClass(20,"abcd")
print("num : ",ob1.num)
print("num : ",ob1.str)
ob2=MyClass(10,"Aishori")
print("num : ",ob2.num)
print("num : ",ob2.str)
ob3=ob1+ob2
print(ob3.num,ob3.str)
ob4=ob1+3
print(ob4.num,ob4.str)
ob5=3+ob2
print(ob5.num,ob5.str)





           
