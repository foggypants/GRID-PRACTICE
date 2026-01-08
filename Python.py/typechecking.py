class calculator:
    def add(self,*args):
        if isinstance(args[0],int) and isinstance(args[1],int):
            print("Addition:",args[0]+args[1])
        elif isinstance(args[0],str) and isinstance(args[1],str):
            print("Concatenation:",args[0]+args[1])
        else:
            print("Invalid input types")
c=calculator()
c.add(5,10)
c.add("Hello, ","World!")
c.add("Hello",13)