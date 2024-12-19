num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
oper = input("Enter the operation +, -, *, / : ")

if oper == "+" :
    def add():
        return(num1+num2)
    print(add())

elif oper == "-" :
    def subtract():
        return(num1-num2)
    print(subtract())

elif oper == "*" :
    def multiply():
        return(num1*num2)
    print(multiply())

elif oper == "/" :
    def divide():
        return(num1/num2)
    print(divide())

else: 
    print("Invalid entry")