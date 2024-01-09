from datetime import date

def celebrate_BD_victory_day ():
    print("Happy Victory Day of Bangladesh!")

today = date.today()
d2 = today.strftime("%B %d, %Y")
print("Today is", d2)

if today.strftime("%B %d")=="December 16":
    celebrate_BD_victory_day()
else:
    pass