print("what type of adventure")
adventure = input()

if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest")

if (adventure == "safe") or (adventure == "long"):
    print("taking the safe route!")

else:
    print("not sure which route to take")

print("what did i hear")
noise = input()

if (noise == 'grrr') or (noise == 'two red eyes'):
    print ("there is a scary creature. I should get out of here!")

else:
    print("I am a little scared but i will continue")
