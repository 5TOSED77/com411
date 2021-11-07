print("is your seat belt on")
seatbelt = input()

if (seatbelt == "not on") or (seatbelt == "unbuckled"):
    print("dont think about starting that car mate")
else:
    if (seatbelt == "on") and (seatbelt == "buckled"):
        print("start your car mate")

petrolcounter = int(input("how full is your petrol tank"))

if petrolcounter <= 5:
    print("you aint got enough go and top up")
elif petrolcounter == 6:
    print("thats the right size mehn")
if petrolcounter not == 7:
        print("your full up and good to go")
