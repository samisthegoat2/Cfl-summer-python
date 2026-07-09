def eat(marshmellows):
   hours = 0
   while marshmellows > 0:
        marshmellows -= 2
        hours += 1
   return hours
           

def main():
    marshmellows = 30
    print(eat (marshmellows))
main()