idMore = 0
anoMore = 0
mesMore = 0

while True:
    list = input().split(' ')
    if list[0] == "0":
        break

    else:
        id = list[0]
        mesEntry = int(list[1])
        anoEntry = int(list[2])
        mesOut = int(list[3])
        anoOut = int(list[4])
        anoTotal = (anoOut - anoEntry)

        if mesEntry == mesOut:
            anoTotal += 1

        if anoTotal == anoMore:
            if mesEntry < mesOut:
                anoTotal += 1
                mesTotal = mesEntry - mesOut
                anoMore = anoTotal
                mesMore = mesTotal
                idMore = id

            else:
                mesTotal = (mesOut - mesEntry) - 12
                if mesTotal > mesMore:
                    anoMore = anoTotal
                    mesMore = mesTotal
                    idMore = id

        elif anoTotal > anoMore:
            anoMore = anoTotal
            idMore = id

print(idMore)
