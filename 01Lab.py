# """ 
# Design a Calculator class that supports basic arithmetic operations.  

# Requirements:
# 1. Attributes:
#    num1: The first number.  
#    num2: The second number.  

# 2. Methods: 
#    add(): Returns the sum of num1 and num2.  
#    subtract(): Returns the difference between num1 and num2.  
#    multiply(): Returns the product of num1 and num2.  
#    divide(): Returns the quotient of num1 and num2. If num2 is zero, it should handle the division error properly.  

# Task:
# Read two numbers from the user as input.  
# Create an instance of the Calculator class with the given numbers.  
# Call each method (add(), subtract(), multiply(), and divide()) and display the results.
# Input
# The first line of input contains two space-separated values: num1 and num2.
# Output
# Perform all four described operations in a given order on the given two numbers and print the results of each operation in a new line.

# Note: divide() should return -1, if num2 is 0.
# Example
# Input
# 6 3
# Output
# 9
# 3
# 18
# 2
# Explanation
# Perform all four operations in the given order:
# add() = 6 + 3 = 9
# subtract() = 6 - 3 = 3
# multiply() = 6 * 3 = 18
# divide() = 6 / 3 = 2

# """

# class Calculator :
#     def __init__(self,num1,num2):
#         self.num1 = num1
#         self.num2 = num2
    
#     def add(self):
#         return self.num1 + self.num2
    
#     def subtract(self):
#         return self.num1 - self.num2
    
#     def multiply(self):
#         return self.num1 * self.num2

#     def divide(self):
#         if self.num2 == 0:
#             return -1
#         return self.num1 // self.num2 
    
# num , num2 = map(int,input().split())
# object_calculator = Calculator(num,num2)

# print(object_calculator.add())
# print(object_calculator.subtract())
# print(object_calculator.multiply())
# print(object_calculator.divide())


# """ 
# Design a Restaurant class to manage menu items effectively. Your task is to implement the class with the following attributes and methods:

# Attributes:
# menu: A dictionary to store menu items and their respective prices, where the key is the item's name, and the value is the price.
# Methods:
# add_item(name, price):

# Adds a new item with its price to the menu.
# If the item already exists, update its price.
# Print "Item added/updated successfully" after adding or updating.
# remove_item(name):

# Removes an item from the menu.
# Print "Item removed successfully" after removing.
# If the item does not exist, print "Item not found".
# display_menu():

# Displays all available menu items with their prices in the format:
# Item Name: Price
# If the menu is empty, print "The menu is empty.".
# Input
# First line contains the name and price of item1, separated by a space.
# Second line contains the name and price of item2, separated by a space.
# Third line contains the name and price of item3, separated by a space.
# Fourth line contains the name of the item to be removed.
# Output
# After adding or updating an item, print:
# "Item added/updated successfully"
# If an item is removed, print:
# "Item removed successfully"
# If the item is not found, print:
# "Item not found"
# Display the menu using display_menu() after performing all operations.
# Example
# Input
# Pizza 500
# Burger 300
# Pasta 400
# Burger

# Output
# Item added/updated successfully
# Item added/updated successfully
# Item added/updated successfully
# Item removed successfully
# Menu:
# Pizza: 500
# Pasta: 400

# """

# class Restaurant:
#     def __init__(self):
#         self.menu = {}


#     def add_item(self, name, price):
#         self.menu[name] = price
#         print("Item added/updated successfully")


#     def remove_item(self, name):
#         if name in self.menu:
#             del self.menu[name]
#             print("Item removed successfully")
#         else:
#             print("Item not found")

#     def display_menu(self):
#         if not self.menu:
#             print("The menu is empty.")
#         else:
#             print("Menu:")
#             for key,value in self.menu.items():
#                 print(f"{key}: {value}")


# restaurant = Restaurant()

# for i in range(3):
#     name, price = input().split()
#     restaurant.add_item(name, price)

# remove_name = input()
# restaurant.remove_item(remove_name)
# restaurant.display_menu()


class Merger:
    def __init__(self,n,m,arr1,arr2,even,odd):
        self.arr1 = arr1
        self.arr2 = arr2
        self.n = n 
        self.m = m
        
    def mergeByParity(self): 
        i , j  , merged = 0, 0, []
        
        while i < self.n or j < self.m:
            if j == self.m or (i < self.n and self.arr1[i] <= self.arr2[j]):
                merged.append(self.arr1[i])
                i += 1
            else:
                merged.append(self.arr2[j])
                j += 1

        even, odd = [], []
        for num in merged:
            (even if num % 2 == 0 else odd).append(num)

        return even + odd

        
        
n,m = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

obj = Merger(n,m,arr1,arr2)
print(obj.mergeByParity())