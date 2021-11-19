distance = int(input("how far are you from the cave?"))
print(distance)

for count in range(8, 1, 1):
    if distance == count:
        print("steps remaining" + 'count')

