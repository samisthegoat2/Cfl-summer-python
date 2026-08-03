def getuserage():
    while True:
        try:
            age = int(input("please put in your age: "))
            if age <= 0:
                print("Invalid age< please try again")
                return age
        except ValueError:
            print("invalid age, please try again")