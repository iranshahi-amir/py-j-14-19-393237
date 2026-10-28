





ghad = float(input("ghad ro bego: "))  #ghad be metr vared shavad
vazn = float(input("vazn ro bego: "))

bmi = vazn/(ghad**2)

if 18.5>bmi:
    print("kambod vazn")

elif 18.5<=bmi<=25:
    print("vazn monaseb")

elif 25<bmi<=30:
    print("ezafe vazn")

else:
    print("chaghy")