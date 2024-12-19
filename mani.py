try :
    num1, num2 = eval(input("Enter 2 numbers, separated by comma: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError :
    print("Division by 0 error!!!")

except SyntaxError :
    print("Syntax error!!! Maybe comma is mising .")

except :
    print("Something went worng")

else :
    print("No exception")

finally :
    print("No metter what it will be outputed")