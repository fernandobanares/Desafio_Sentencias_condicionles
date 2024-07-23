
peso = float(input("Ingrese su peso en kg:\n"))
altura_cm = float(input("Ingrese su altura en centímetros:\n"))

altura_m = altura_cm / 100

IMC = peso/altura_m ** 2
IMC = round(IMC, 2)

if IMC < 18.5:
    print(f"Su IMC es {IMC} y indica que está Bajo Peso")
elif 25 > IMC >= 18.5:
    print(f"Su IMC es {IMC} y indica que está en un peso adecuado")
elif 30 > IMC >= 25:
    print(f"Su IMC es {IMC} y indica que está con sobrepeso")
elif 35 > IMC >= 30:
    print(f"Su IMC es {IMC} y tiene Obesidad grado I")
elif 40 > IMC >= 35:
    print(f"Su IMC es {IMC} y tiene Obesidad grado II")
else:
    print(f"Su IMC es {IMC} y tiene Obesidad grado III")
