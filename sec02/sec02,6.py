





while True:
    num1 = float(input("adad avaleto bego: "))
    num2 = float(input("adad dovometo bego: "))
    amalgar = input("amaliat (-,+,*,/,**): ")
    if amalgar == "-":
        print(("natije = "), num1 - num2)
    elif amalgar == "+":
        print(("natije = "), num1 + num2)    
    elif amalgar == "*":
        print(("natije = "), num1 * num2)
    elif amalgar == "**":
        print(("natije = "), num1 ** num2)
    elif amalgar == "/":
        if num2 != 0:
            print(("natije = "), num1 / num2)
        else:
            print("dar riazi tarif nashode")
    else:
        print("amalgar dar in mashin hesab tarif nashode")

    while True:
        dobare = input("edame bedim (are/na): ")

        if dobare == "na":
            break
        elif dobare == "are":
            break
        else:
            print("faghad are ya na vared kon")
    if dobare == "na":
        break