#Exercicio1: Converter Segundos em Horas, Minutos e Segundos
#Enunciado: Desenvolva um programa que assuma uma entrada em segundos e a converta para horas, minutos e segundos

SegundosInseridos = int(input("Insira segundos: "))

horas = SegundosInseridos // 3600          # // --> divisão inteira
resto = SegundosInseridos % 3600           #fazer o resto porque depois de calcular as horas vamos calcular os minutos c o que sobra
minutos = resto // 60
segundos = resto % 60

#print(f"Horas: {horas}, Minutos: {minutos}, Segundos: {segundos}")

print(f"{horas}h  {minutos}m  {segundos}s")