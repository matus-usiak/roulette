import random

credit = int(input("Please enter your credit "))

while credit > 0:
    bet = input(
        "Place your bets in form of bet type and amount.\n"
        "Bet types are: single number, red, black, odd, even, 1 to 18, 19 to 36 followed by space separated by "
        "semicolon.\n "
        "For example: 18 20;odd 10; black 30\n"
        "Your bet: ")

    betlist = bet.split(";")

    betamountlist = []
    bettypelist = []
    for bt in betlist:
        bettypelist.append(bt.split(" ")[0])
        betamountlist.append(bt.split(" ")[1])

    totalbet = sum(map(int, betamountlist))

    # spinresult = int(random.randint(0, 36))
    spinresult = 5
    print("Spin result: ", spinresult)

    redspaces = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    spinresultlist = [str(spinresult)]

    if spinresult in redspaces:
        spinresultlist.append("red")
    if spinresult % 2 ==0:
        spinresultlist.append("even")
    if spinresult not in redspaces:
        spinresultlist.append("black")
    if spinresult % 2 == 1:
        spinresultlist.append("odd")
    if spinresult <= 18:
        spinresultlist.append("1 to 18")
    else:
        spinresultlist.append("19 to 36")

    winningamount = 0

    i = 0
    while i < len(betlist):
        if betlist[i].split(" ")[0] in spinresultlist:
            print("Pay for: ", betlist[i].split(" ")[0])
            print("x", betlist[i].split(" ")[0])
            print("y", int(betamountlist[i]))
            print("bet type list", bettypelist[i])
            if bettypelist[i] in spinresultlist:
                if bettypelist[i] in ["red", "black", "even", "odd", "1 to 18", "19 to 36"]:
                    winningamount = winningamount + int(betamountlist[i]) + (int(betamountlist[i]) * 2)
                if spinresultlist[0] in betlist[i].split(" ")[0]:
                    winningamount = winningamount + int(betamountlist[i]) + (int(betamountlist[i]) * 36)
                if bettypelist[i] not in ["red", "black", "even", "odd", "1 to 18", "19 to 36"]:
                    winningamount = winningamount - int(betamountlist[i])
                if spinresultlist[0] not in betlist[i].split(" ")[0]:
                    winningamount = winningamount - int(betamountlist[i])
        i = i + 1
    print("Total winning: ", winningamount)
    print("total bet ", totalbet)
    # hahaha
else:
    print("No credit")