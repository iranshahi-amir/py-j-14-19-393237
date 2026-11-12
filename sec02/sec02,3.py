




number = int(input("adad bego: "))

if number > 1:
    for i in range(2,number):
        if number % i == 0:
            print("adad aval nist")
            break
    
    else:
        print("adad aval hast")
else:
    print("adad aval nist")
