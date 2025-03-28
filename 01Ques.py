'''

Design a Rectangle class to represent a rectangle and calculate its area and perimeter. The class should include the following:

Attributes:
​​​length: The length of the rectangle.
width: The width of the rectangle.
 
Methods:
area(): Calculates and returns the area of the rectangle.
perimeter(): Calculates and returns the perimeter of the rectangle.

***************       Task:      ***************

- Read the length and width of the rectangle from the input.
- Create an instance of the Rectangle class by providing the length and width.
- Use the area() method to compute the rectangle's area.
- Use the perimeter() method to compute the rectangle's perimeter.



Input
The first line of input contains two space-separated values: the length and width of the rectangle.
Output
Print the desired Output
Example
Input
3 5

Output
15
16

'''

class Rectange:
    def __init__(self,length,width):
        self.length = length
        self.breadth = width
        
    def area(self):
        return self.length * self.breadth
    
    def perimeter(self):
        return 2 * ( self.length + self.breadth)
    
length,width = map(int,input().split())
variable = Rectange(length,width)
print(variable.area())
print(variable.perimeter())


"""  

Design an Employee class to represent employees and calculate their annual salary. The class should include the following:

Attributes: 
name: The name of the employee.
salary: The monthly salary of the employee.

Method:
annual_salary(): Calculates and returns the annual salary by multiplying the monthly salary by 12.
 
Note:-
You do not need to create an instance of the Employee class or manually call the annual_salary() method. You only need to implement the class structure and the method as specified. The class will be tested with predefined values, and the annual_salary() method will be automatically called in the background for testing purposes. 

Input
The first line contains a string representing the name (e.g., Animay).
The second line contains an integer representing the value (e.g., 20000).
Output
A single integer result based on the required calculation (e.g., 240000).
Example
Input
Animay
20000

Output
240000


"""

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def annual_salary(self):
        return 12 * self.salary
    
name = input()
salary = int(input())
         
object = Employee(name,salary)

print(object.annual_salary())