
import random
import matplotlib.pyplot as plt
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod 

#Creating the superclass called Shape
class Shape(ABC):
    def __init__(self):
        self.__color = "red"   # setting the default color to red

    def set_color(self, color):    #setter function
        self.__color = color
    
    def get_color(self):             #getter function
        return self.__color
    
    @abstractmethod   #this just indicates that the following method is abstract

    def find_area(self):
        pass

    @abstractmethod   #this just indicates that the following method is abstract

    def find_volume(self):
        pass
    
    def display():
        pass

# Creating subclass Circle
class Circle(Shape):
    
    def __init__(self):        # we set the private attribute for the subclass
        super().__init__()
        self.__radius = 1           # the default value
    
    def set_radius(self, radius):    # setter function for the Circle class
        self.__radius = radius
    
    def get_radius(self):             # getter function for the Circle class
        return self.__radius
    
    def find_area(self):
        return 3.14 * self.__radius ** 2    # we use the formula of finding the area of the circle
    
    def find_volume(self):
        return "The circle cannot have a volume"
    
    def display(self):                 # display function will print the class name
        return "Circle type"

# Creating subclass Square
class Square(Shape):
    def __init__(self):        # we set the private attribute for the subclass
        super().__init__()
        self.__side = 2.3           # the default value
    
    def set_side(self, side):    # setter function for the Square class
        self.__side = side
    
    def get_side(self):             # getter function for the Square class
        return self.__side
    
    def find_area(self):
        return self.__side ** 2    # we use the formula of finding the area of the square
    
    def find_volume(self):
        return "The square cannot have a volume"
    
    def display(self):                 # display function will print the class name
        return "Square type"


# Creating subclass Cube
class Cube(Shape):
    def __init__(self):        # we set the private attribute for the subclass
        super().__init__()
        self.__lenght = 7
        self.__width = 7
        self.__height = 7          # the default values
    
    def set_lenght(self, lenght):    # setter function for the Cube class
        self.__lenght = lenght

    def set_width(self, width):    # setter function for the Cube class
        self.__width = width

    def set_height(self, height):    # setter function for the Cube class
        self.__height = height
    
    def get_lenght(self):    # setter function for the Cube class
        return self.__lenght

    def get_width(self):    # setter function for the Cube class
        return self.__width

    def get_height(self):    # setter function for the Cube class
        return self.__height
    
    def find_area(self):
        return 6 * self.__lenght ** 2    # we use the formula of finding the area of the cube
    
    def find_volume(self):
        return self.__height * self.__lenght * self.__width         # we use the formula of finding the volume of the cube
    
    def display(self):                 # display function will print the class name
        return "Cube type"
    
list_shapes = []   # the list 

circle_shape = 0   
square_shape = 0
cube_shape = 0

# Creating the list of 15 objects 
for s in range(0,15):
    random_option = random.randint(1,3)    # randomly choosing a number from 1 to 3 
    if random_option == 1:
        shape = Circle()
        circle_shape += 1   # finding out how many shapes of circle there are to be able to create the pie chart 
    elif random_option == 2:
        shape = Square()
        square_shape += 1    # finding out how many shapes of square there are to be able to create the pie chart 
    else:
        shape = Cube()
        cube_shape +=1        # finding out how many shapes of cube there are to be able to create the pie chart 
    list_shapes.append(shape)    # adding the shapes to the list


# Creating the pie chart diagram
def pie_chart():
    num_shapes = [circle_shape, square_shape, cube_shape]     # creating a list with the numbers of each shape
    shape_name = ["Circle Shapes", "Square Shapes", "Cube Shapes"]    # creating a list for the labels of the slices
    plt.pie(num_shapes, labels = shape_name)      # creating a pie chart from the values colected
    plt.title('Objects Created')    # adding a title 
    plt.show()      # displaying the pie chart 


# Creating this so the messagebox can be created
mess_box = []
for shape in list_shapes:
    if isinstance(shape, Cube):
        mess_box.append(shape.display())  # adding to the messagebox
        mess_box.append("The Volume is " + str(shape.find_volume()))      # adding to the messagebox      
    else:
        mess_box.append(shape.display())           # adding to the messagebox
        mess_box.append("The Area is " + str(shape.find_area()))      # adding to the messagebox
    

messagebox_result = "\n".join(mess_box)



# Print all the options for display
print("You can observe the result in 3 ways:")
print("a. Python Console")
print("b. Save the result into a file and input the file name")
print("c. Print the result into one GUI messagebox window")
display = input("How would you like to view the result? Select a, b, or c: " )   # asking the user to select the display


if display == "a":       # display in Python Console
    for shape in list_shapes:
        if isinstance(shape, Cube):
            print (shape.display())
            print ("The Volume is " + str(shape.find_volume()))
        else:
            print (shape.display())
            print ("The Area is " + str(shape.find_area()))
elif display == "b":         # Save to a file and ask the user to input the file name
    file_name = input("What is the file name?")   # Asking the user to enter the file name
    file = open (file_name, "w")    # Open the file in write mode 
    for shape in list_shapes:            # Following is the code to write the results in the file
        if isinstance(shape, Cube):
            file.write(shape.display() + "\n")
            file.write("The Volume is " + str(shape.find_volume()) + "\n")
        else:
            file.write(shape.display() + "\n")
            file.write("The Area is " + str(shape.find_area()) + "\n")
    file.close()
else:
    messagebox.showinfo("Shape Results", messagebox_result)   # display the messagebox

pie_chart()  # Calling the function at the end so it pops up after the display option is selected. 





