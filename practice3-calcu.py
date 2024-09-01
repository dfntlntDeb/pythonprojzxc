def operation(case,num1, num2):
    match case:

        case "Add":
            addition(num1,num2)
        case "Subtract":
            subtraction(num1,num2)
        case "Multiply":
            multiplication(num1,num2)
        case "Divide":
            division(num1,num2)
    
def addition(num1,num2):
    sum = int(num1 + num2)
    print("The sum of",num1,"and",num2,"is",sum)

def subtraction(num1,num2):
    difference = int(num1 - num2)
    print("The difference of",num1,"and",num2,"is",difference)

def multiplication(num1,num2):
    product = int(num1 * num2)
    print("The sum of",num1,"and",num2,"is",product)

def division(num1,num2):
    qoutient = int(num1 / num2)
    print("The qoutient of",num1,"and",num2,"is",qoutient)

while(True):
    
    case = input("What operation do you want use? ").title()
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    operation(case,num1,num2)

    cntnue = input("Do you want to continue? (Y/N) ").title()
    if (cntnue == 'Y'):
        continue
    else:
        print("Okeh goodbye!")
        break