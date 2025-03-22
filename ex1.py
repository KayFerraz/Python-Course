#Crie um algoritmo, que pede ao usuário 4 notas do 
# #semestre da faculdade. Calcule e só mostre a média entre essas notas

nota1 = int( input("Digite a primeira nota: "))
nota2 = int ( input("Digite a segunda nota: "))
nota3 = int (input("Digite a terceira nota: "))
nota4 = int (input("Digite a quarta nota: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma // 4
print (f"A média é de {round(media,2)}")