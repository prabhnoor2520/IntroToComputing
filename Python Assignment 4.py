#Q1 Tower of Hanoi
def TowerOfHanoi(n , Tower1, Tower3, Tower2):
	if n == 0:
		return 0
	TowerOfHanoi(n-1, Tower1, Tower2, Tower3)
	print("Move disk",n,"from rod",Tower1,"to rod",Tower3)
	TowerOfHanoi(n-1, Tower2, Tower3, Tower1)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print()


#Q2 Pascal Triangle

#Recursive Procedure

def pascals_triangle(n):
    """ Defining a function to return an array containing
        the first n rows of PASCAL's TRIANGLE. """

    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        next_row = [1]
        result = pascals_triangle(n - 1)
        last_row = result[-1]

        for i in range(len(last_row) - 1):
            next_row.append(last_row[i] + last_row[i + 1])

        next_row += [1]
        result.append(next_row)
        return result

number_of_rows = int(input("Enter the number of rows you want:"))

if number_of_rows < 0:
    print("Number of rows cannot be negative.")
    exit()

arr = pascals_triangle(number_of_rows)
width = len(str(arr[-1])) - 2

for i in arr:
    string = ""

    for j in i:
        string += (f"{j}" + "   ")

    print(string.center(width * 2, " "))

# Iterative Procedure.

number_of_rows = int(input("Enter the number of rows you want:"))

if number_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

arr = [[1]]

while len(arr) < number_of_rows:

    next_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        next_row.append(last_row[i] + last_row[i + 1])

    next_row += [1]
    arr.append(next_row)

width = len(str(arr[-1])) - 2
for i in arr:
    string = ""

    for j in i:
        string += (f"{j}" + "   ")

    print(string.center(width * 2, " "))

print()  


#Q3
int1 = int(input("Enter the first integer:"))
int2 = int(input("Enter the second integer:"))

result=divmod(int1, int2)

print(f"The Quotient is {result[0]}.\nThe remainder is {result[1]}.")

#Q3a                                         

if callable(divmod):
    print("It's callable")
else:
    print("It's not callable")

#Q3b

if 0 in [int1, int2] + list(result):
    print("All the values are not non-zero.")

elif 0 not in [int1, int2] + list(result):
    print("All the values are non-zero.")

#Q3c

result_list = list(result)

for i in (4, 5, 6):
    result_list.append(i) 

new_result_list=[]
for j in result_list:
    if j>4:
        new_result_list.append(j)
print('Values greater than 4 are', new_result_list)

#Q3d   
converted_set = set(new_result_list)
print(f"Converted Set : {converted_set}")

#Q3e
print("Immutable Set :", frozenset(converted_set))

#Q3f

print("Maximum value of the following numbers is", max(converted_set))

print("Hash value of max value is", hash(max(converted_set)))

print()    



#Q4
class Students:

    def __init__(self, name:str, rollno:int):
        self.name=name
        self.rollno=rollno

    def __del__(self):
        print('Object Destroyed')


name=input('Enter name:')
rollno=int(input('Enter roll number:'))

stu=Students(name,rollno)      

print(f"Student name is: {stu.name} and roll number is {stu.rollno}")



#Q5
class Employees:

    def __init__(self, name: str, salary:int ):
        self.name=name
        self.salary=salary

    def __del__(self):                   
        print('Object destroyed')

Mehak = Employees("Mehak", 40000)
Ashok = Employees("Ashok", 5000)
Viren = Employees("Ashok", 60000)

print(f"Employee name is {Mehak.name} and salary is {Mehak.salary}")
print(f"Employee name is {Ashok.name} and salary is {Ashok.salary}")
print(f"Employee name is {Viren.name} and salary is {Viren.salary}")


#Q5a

Mehak.salary=7000                                                         #Viren's salary updated              
print(f"Employee name is {Mehak.name} and salary is {Mehak.salary}")

#Q5b

del Viren                #Viren's record deleted
print()                                            




#Q6
George_word = input("Enter the word entered by George:").lower().strip()  

Barbie_word = input("Enter the word entered by Barbie:").lower().strip()

George_list = list(George_word)
Barbie_list = list(Barbie_word)

George_list.sort()
Barbie_list.sort()

if len(George_word)!=len(Barbie_list):          #if both words are same
    print('Letters of both word are not same.\n their friendship is fake.')

elif George_word==0:          #if user gives empty input
    print('No input from user.')

elif Barbie_list==George_list:                  #true friendship
    print('Result: Their friendship is true.')

else:                                      
    print('Result: Their friendship is fake')



