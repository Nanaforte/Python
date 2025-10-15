
num1=int(input("Insira o primeiro número: "))
num2=int(input("Insira o segundo número: "))
num3=int(input("Insira o terceiro número: "))

if num1 > num2 > num3:
    print(f"maior: {num1}\nmeio: {num2}\nmenor: {num3}")
elif num1 > num3 > num2:
    print(f"maior: {num1}\nmeio: {num3}\nmenor: {num2}")
elif num2 > num3 > num1:
    print(f"maior: {num2}\nmeio: {num3}\nmenor: {num1}")
elif num2 > num1 > num3:  
    print(f"maior: {num2}\nmeio: {num1}\nmenor: {num3}")
elif num3 > num1 > num2:
    print(f"maior: {num3}\nmeio: {num1}\nmenor: {num2}")
elif num3 > num2 > num1:
    print(f"maior: {num3}\nmeio: {num2}\nmenor: {num1}")



'''
max = max(num1,num2,num3)
min = min(num1,num2,num3)
print(f"Maior num {max} e menor num {min}")
'''

