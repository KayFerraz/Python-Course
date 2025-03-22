 #Crie um algoritmo que pede ao usuário 2 números, 
 # e exiba o resultado final no seguinte formato: X / Y = resultado

num1 = int (input("Digite o primeiro número: "))
num2 = int (input("Digite o segundo número: "))

divisao = num1 /num2

print(f"{num1} / {num2} = {round(divisao,2)}")