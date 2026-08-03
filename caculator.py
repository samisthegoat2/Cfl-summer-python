def multiply(x,y):
   total = 0
   total = x * y
   return total







def main():
    x = int(input("please choose a number: "))
    y = int(input("please choose a number:"))
    operation = input("please choose a sign")
    if operation == "*":
        print(multiply (x,y))
    #lif operation == "-":
       #print(subtract(x,y))
    #lif operation == "+":
       #print(addition(x,y))
    

     
     
main()