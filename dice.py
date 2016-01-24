import random

#x = input()
while 1:
    x = random.randint(1,6)
    print(x)
    while 1:
        print ("da li zelite da bacate ponovo? (da/ne)")
        temp = raw_input()
        if temp in ["da", "DA"]:
            break
        elif temp in ["ne", "NE"]:
            exit(1)


