#Q1
String="Python is a case sensitive language"

#1a 
print(len(String))

#1b 
print(String[::-1])

#1c
String_1=String[10:26]
print(String_1)

#1d
print(String.replace("a case sensitive","object oriented"))

#1e
print(String.find("a"))

#1f
print(String.replace(" ",""))

#Q2
name=input("enter your name:")
SID=int(input("enter your SID:")) #SID = Student ID
Dept=input("enter department name:") #Dept= Department Name
CGPA=float(input("enter your CGPA:"))

print("Hey, %s Here! \nMy SID is %d \nI am from %s and my CGPA is %f"%(name,SID,Dept,CGPA))
    

#Q3
a=56
b=10

#3a AND 
print(a&b) 

#3b OR
print(a|b) 

#3c XOR
print(a^b) 

#3d Left Shift
print(a<<2)
print(b<<2) 

#3e 
print(a>>2) #Left Shift
print(b>>4) #Right Shift


#Q4 To determine which number is greatest

Number_1=int(input("enter your first number:"))
Number_2=int(input("enter your second number:"))
Number_3=int(input("enter your third number:"))

if  Number_1>=Number_2 and Number_1>=Number_3:
    print("Number_1 is the greatest")
elif Number_2>=Number_1 and Number_2>=Number_3:
    print("Number_2 is the greatest")
else:
    print("Number_3 is the greatest")
    

    
#Q5 To check 'name' in string
    
string=input("enter a string:")

if 'name' in string:
    print("yes")
else:
    print("no")

    

#Q6 To check if formation of triangle is possible
side1=int(input("enter length of 1st side:"))
side2=int(input("enter length of 2nd side:"))
side3=int(input("enter length of 3rd side:"))

if (side1 + side2)>side3 and (side1 + side3)>side2 and (side2 + side3)>side1:
    print("Yes, formation of triangle is possible")
else:
    print("No, formation of triangle is not possible")
    
    





