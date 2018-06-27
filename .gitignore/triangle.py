"""
>>> This program is to accept three inputs from the user which
are considered as three sides of triangle. The input entered
by user is rounded to three decimal values and this message is
given to the user.

>>> The sides are validated and then user is given result as
to whether the triangle is Equilateral or Isosceles or Scalene.

>>> The program will exit if the inputs are invalid i.e.
negative or zero or null values.

>>> The sides also should satisfy the triangle theorm i.e. sum
of two sides should be greater than the third side.

"""

import sys
class Triangle(object):
    
    """ Initialization of attributes in class constructor below """
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    """ Method to validate input values for each side entered by the user """
    def validate_input(self):
        try:
            if ((self.side1 <= 0) | (self.side2 <= 0) | (self.side3 <= 0)):
                raise ValueError
        except ValueError:
            print ('Cannot have zero or a negative number as input')
            sys.exit() 
        else:
            print ('Valid input parameters')

    """ Method to apply triangle theorm, checks if sides can form a triangle """
    def validate_triangle(self):
        try:
            if ((self.side1 + self.side2 <= self.side3) |
                (self.side2 + self.side3 <= self.side1) |
                (self.side3 + self.side1 <= self.side2)):
                raise ValueError
        except ValueError:
            print ('The sides violated triangle theorm, cannot form a triangle')
            sys.exit()  
        else:   
            print ('The inputs can form a triangle')
            
    """ Method to evaluate the type of triangle """
    def type_triangle(self):
        """ Method to validate of input parameters """
        self.validate_input()
        self.validate_triangle()
        if ((self.side1 == self.side2) & (self.side2 == self.side3)):
            return "Equilateral triangle"
        elif ((self.side1 == self.side2) |
              (self.side2 == self.side3) | (self.side3 == self.side1)):
            return "Isosceles triangle"
        else:
            return "Scalene triangle"            

    """ Main method where execution starts """
def main():
    try:
        """ Accepting values of sides of traingle from user.
            The value would be rounded to three decimals
            for pictorial representation """
        print ('User input is rounded to three decimals ' )        
        side1 = round(float(input('Enter the value of side1 of traingle : ')), 3)
        side2 = round(float(input('Enter the value of side2 of traingle : ')), 3)
        side3 = round(float(input('Enter the value of side3 of traingle : ')), 3)
    except:
        print ('Input values not meaningful' , sys.exc_info())
        sys.exit()
        
    """ Initialization of instance of the class Triangle """
    traingle_test = Triangle(side1,side2,side3)
    result = traingle_test.type_triangle()
    
    """ Print the final output """
    print ('The type triangle based on the inputs is : ' + result)

    """ Execution of the program """
if __name__ == "__main__":
    main()
        
        
        
        
    
    
