





ghad = float(input("ghad ro bego: "))  #ghad be metr vared shavad
vazn = float(input("vazn ro bego: "))

bmi = vazn/(ghad**2)

if ghad<=0 or vazn<=0:
    print("eshtebah vared kardid")

elif 18.5>bmi:
    print("kambod vazn", bmi)

elif 18.5<=bmi<=25:
    print("vazn monaseb", bmi)

elif 25<bmi<=30:
    print("ezafe vazn", bmi)

else:
    print("chaghy", bmi)