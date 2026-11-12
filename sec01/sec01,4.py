



d = input("esm mashinet ro bego: ")

a = float(input("zarfiat bak ro bego: "))

b = float(input("masraf sokht to har 100km ro bego: "))

if a < 0 or b < 0:
    print("eshtebah vared kardid")

else:
    c = (a/b)*100
    print(d,"=","masafat:",c)

