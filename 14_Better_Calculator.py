num1 = float(input("First number: "))
op = input("Operator: ")
num2= float(input("Second number: "))
#if(op.isdigit()):
    print("jest ok")
# else:


if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1-num2)
elif op == "/":
    print(num1/num2)
elif op == "+":
    print(num1*num2)

else:
    print("Invalid Operator")
