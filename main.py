import random

credit = int(input("Please enter your credit: "))

if credit < 0:
    print("Invalid input! Please enter a number greater than 0.")

while credit > 0:
    bet = input(
        "Place your bets in form of <bet type><space><amount> separated by semicolon.\n"
        "Bet types are: single number, red, black, odd, even, 1to18, 19to36. \n"
        "For example: 18 20;odd 10; black 30\n\n"
        "Your bet: ")

    betlist = bet.split(";")

    betamountlist = []
    bettypelist = []
    for bt in betlist:
        bettypelist.append(bt.split(" ")[0])
        betamountlist.append(bt.split(" ")[1])

    totalbet = sum(map(int, betamountlist))

    if totalbet > credit:
        print("Not enough credit!")

    spinresult = int(random.randint(0, 36))

    redspaces = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

    spinresultlist = [str(spinresult)]

    print("Spin result: ", spinresult, " - ", spinresultlist)

    if spinresult in redspaces:
        spinresultlist.append("red")
    if spinresult % 2 == 0:
        spinresultlist.append("even")
    if spinresult not in redspaces:
        spinresultlist.append("black")
    if spinresult % 2 == 1:
        spinresultlist.append("odd")
    if spinresult <= 18:
        spinresultlist.append("1to18")
    else:
        spinresultlist.append("19to36")

    winningamount = 0

    i = 0
    while i < len(betlist):
        if bettypelist[i] in spinresultlist:
            winningamount = winningamount + int(betamountlist[i]) + (int(betamountlist[i]) * 2)

        if spinresultlist[0] in betlist[i].split(" ")[0]:
            winningamount = winningamount + int(betamountlist[i]) + (int(betamountlist[i]) * 35)

        if bettypelist[i] not in spinresultlist:
            winningamount = winningamount - int(betamountlist[i])

        i = i + 1
    credit = credit + winningamount
    print("Spin result: ", spinresult, " - ", spinresultlist)
    print("Bet amount: ", totalbet)
    print("Return: ", winningamount)
    print("Remaining credit: ", credit)
else:
    print("No credit")
