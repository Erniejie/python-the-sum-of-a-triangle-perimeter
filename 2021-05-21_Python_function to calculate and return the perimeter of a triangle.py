#function to calculate and return the perimeter of a triangle Python
"ComputerProgrammming Tutor,May18,2021"

def CalculateTrianglePerimeter(a,b,c):
    perimeter = a+b+c
    return perimeter

#  BODY of Python Code
a = int(input("Enter the Length of  first Side, a: "))
b = int(input("Enter the Length of  Second Side, b: "))
c = int(input("Enter the Length of  Third Side, c: "))

perimeter = CalculateTrianglePerimeter(a,b,c)

print("The Perimeter of the triangle is:" + str(perimeter ))

#rounding up/Down Functions:



#math.floor(1.2)
#math.ceil(1.2)
#"%.2f"%

      
