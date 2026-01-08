class Calculator:
    def add(self,*args):
        choose=input("choose the operator(*,+,-,/): ")
        if choose=="+":
            print("Addition:",sum(args))
        elif choose=="-":
            print("Subtraction:",args[0]-args[1])
        elif choose=="*":
            print("Multiplication:",args[0]*args[1])
        elif choose=="/":
            print("Division:",args[0]/args[1])
        else:
            print("Invalid operator")
c=Calculator()
c.add(int(input("Enter first number: ")),int(input("Enter second number: ")))
