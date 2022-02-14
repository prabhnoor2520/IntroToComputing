#Q1 to check characters

String_1=str(input("Enter a String: "))
list=String_1.split() #split
dict={} 
if list.__len__()==1:   #for 1 element
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)   
else:                   #for more than 1 element
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
print("\n")

#Q2 to print next date
def is_leap_year(year: int) -> bool:                                                      #to check leap year 
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Date - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Constraints given in the question
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
    if month in (4,6,9,11) and date == 31:                                                                          
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
    elif month == 2 and date >= 29:                                                                                 #For number of days in FEB
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
if month == 2:                                                                                                    
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if date == max_days:                                                                                                
    date = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
print("Next Date is: %d/%d/%d" % (date,month,year))



#Q3
list_1=[]                                            
n=int(input("enter number of terms:"))          #enter the terms required
for i in range(0,n):
    z=int(input("enter numbers:"))
    list_1.append(z)
list_2=[]
for i in list_1:
    tuple=(i,i**2)
    list_2.append(tuple)
print(list_2)

#Q4
marks=int(input("marks:"))

if(marks>=4 and marks<=10):
    if(marks==4):
        grade="D"
        performance="poor"
    elif(marks==5):
        grade="C"
        performance="below average"
    elif(marks==6):
        grade="C+"
        performance="average"    
    elif(marks==7):
        grade="B"
        performance="good"
    elif(marks==8):
        grade="B+"
        performance="very good"
    elif(marks==9):
        grade="A"
        performance="excellent"
    elif(marks==10):
        grade="A+"
        performance="outstanding"
else:
    print("error")

print("Your grade is ",grade," and your performance is" ,performance)


        
#Q5 to print the given pattern

n = 6

for i in range(n):
   
    for j in range(i):
        print(' ', end='')
    
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()


#Q6   
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}

while True:
    option = input("Do you want to add another student entry(Y or N):").upper()
    if option == 'Y':
        sid = int(input("enter another SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')

#Q6a. print the dictionary
print("<a> Student Details",students)

#Q6b. sort acc to the names
print("<b> Sorted Dictionary According To Student Name :",{k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#part c. sort acc to the SIDs
print("<c> Sorted Dictionary According To Student SID :",{k:v for k,v in sorted(students.items())})

#part d. search for a student by their SID
while True:
    sid = int(input("Search Name with help of SID: "))
    if sid in students:
        print("<d> Name Of The Student Is :",students[sid])
        break
    else:
        print(" Wrong SID Please Check Again")




#Q7
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
no_of_terms=int(input("Enter the number of terms: "))
if no_of_terms <= 0:     # Check if the number of terms are valid
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(no_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)       # average of series
print("Average of the resulting Fibonacci Series",avg)


#Q8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#Q8 a
Set_A = Set1.union(Set2) - Set1.intersection(Set2)
print(Set_A)

#Q8 b
Set_B1 = Set1.difference(Set2.union(Set3))
Set_B2 = Set2.difference(Set1.union(Set3))
Set_B3 = Set3.difference(Set2.union(Set1))

Set_B = Set_B1.union(Set_B2).union(Set_B3)
print(Set_B)

#Q8 c
Set_C1 = Set1.intersection(Set2)
Set_C2 = Set2.intersection(Set3)
Set_C3 = Set1.intersection(Set3)

Set_C = Set_C1.union(Set_C2).union(Set_C3)
print(Set_C)

#Q8 d
Set_I = {1,2,3,4,5,6,7,8,9,10}
Set_D = Set_I.difference(Set1)
print(Set_D)

#Q8 e
Set_U = Set1.union(Set2).union(Set3)
Set_E = Set_I.difference(Set_U)
print(Set_E)




    
