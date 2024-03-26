from datetime import date

def celebrate_BD_victory_day ():
    print("Happy Victory Day of Bangladesh!")
def birthday_celebrate_BD ():
    print("Happy Birthday Day Bangladesh!")

today = date.today()
d2 = today.strftime("%B %d, %Y")
print("Today is", d2)

if today.strftime("%B %d") == "December 16":
    celebrate_BD_victory_day()
elif today.strftime("%B %d") == "March 26":
    birthday_celebrate_BD()
