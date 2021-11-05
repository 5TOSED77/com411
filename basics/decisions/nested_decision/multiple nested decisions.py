location: str=input("Where should I look?")
print(location)

if location == 'in the bedroom':
    print("Where in the bedroom should I look?")

if location == 'under the bed':
    print("Found some shoes but no battery")

else:
    print("found some shoes but no battery")

print('found some mess but no battery')

if location == 'in the bathroom':

    bathroom: str=input("where in the bathroom should i look")
    print(bathroom)

if bathroom == 'in the bathtub':
    print('found a rubber duck but no battery')

else:
    print("found a wet surface but no battery")


if bathroom == 'in the lab':
    print("where in the lab should i look")

    lab: str=input("where in the lab should i look")
    print(lab)

if lab == 'on the table':
    print("Yes! I found my battery!")

else:
    print("found some tools but no battery.")

print("i do not know where that is but i will keep looking")