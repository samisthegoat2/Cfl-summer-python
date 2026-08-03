def people(students):
   hours = 0
   while students > 0:
        students -= 2
        hours += 1
   return hours
           

def main():
    students = 13
    print(people (students))
main()