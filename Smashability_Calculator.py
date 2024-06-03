age = int(input("How old is the user: "))
Gendah = input("What's your gender (Female/Male): ").lower()
race = input ("What's your race (White/Black/Asian/Brown): ").lower()
Unsmashable_list=['white','brown','black']
#underage
if age in range (0,18):
    if Gendah=="female":
        if race=="white":
            print("Smashable ? : No, illegal")
        elif race in Unsmashable_list:
            print("Smashable ? : No, illegal")
        else:
            print("Gender input error")
    elif Gendah=="male":
        if race=="white":
            print("Smashable ? : NO!!, illegal AND gay.")
        elif race in Unsmashable_list:
            print("Smashable ? : NO!!, illegal AND gay.")
        else:
            print("Error race input")
    else:
        print("Error gender input")
#smashable age
elif age in range (18,30):
    if Gendah=="female":
        if race=="white":
            print("Smashable ? : Yes")
        elif race in Unsmashable_list:
            print("Smashable ? : Not racist but unsmashable")
        else:
            print("Race input error")
    elif Gendah=="male":
        if race=="white":
            print("Gay and bad skin color, unsmashable")
        elif race in Unsmashable_list:
            print("Gay and bad skin color, unsmashable")
        else:
            print("Error race input")
    else:
        print("Error Gender input")
#old people
elif age in range (30,100):
    if Gendah=="female":
        if race=="white":
            print("Smashable ? : Yes, but too old")
        elif race in Unsmashable_list:
            print("Smashable ? : Too old, unsmashable anyways because of skin color")
        else:
            print("Race input error")
    elif Gendah=="male":
        if race=="white":
            print("Gay and old, unsmashable")
        elif race in Unsmashable_list:
            print("Gay and old, unsmashable")
        else:
            print("Error race input")
    else:
        print("Error Gender input")
else:
    print("Please input your real age")
        