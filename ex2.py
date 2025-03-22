# Crie um algoritmo, que converte Reais em Dólar. Peça ao usuário o valor que ele deseja converter para Dólar.
#  Exemplo: Digitei 10 reais, calcule 
#quantos dólares eu tenho a partir dos 10 reais. Valor atual do Dólar: $5,73

dolar = int(input("Quantos reais você tem?"))

conversao = dolar * float (5.73)

print (f"Você tem {conversao} dólares")