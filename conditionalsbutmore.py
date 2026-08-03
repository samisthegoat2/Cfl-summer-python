fighter = "wizard"
key = True
energy = 35

if fighter == "warrior" and key == True:
    print("congrats you are allowed to open the door.")
    if energy > 30:
        print("you can open the door, energy is sufficient.")
    elif energy < 30:
        print("you cant open the door, your energy is too low")
    elif energy == 0:
        print("come back tommorow, your enrgy is too low")
        
