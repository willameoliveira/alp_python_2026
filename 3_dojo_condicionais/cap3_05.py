'''
5. Uma empresa concederá um aumento de salário aos seus 
funcionários, variável de acordo com o cargo, conforme a tabela 
abaixo:

Cargo Aumento (%)
Programador de Sistemas 30
Analista de Sistemas 20
Analista de Banco de Dados 15

Crie um programa que solicite ao usuário o salário e o cargo de
um determinado funcionário. 
Na sequência, o programa deve calcular e imprimir o seu novo salário. 
Caso o cargo informado não esteja na tabela, 
o programa deve imprimir “Cargo inválido”.

'''
print("""1.Programador de sistemas:
      2.Analista de sistemas
      3.Anaslita de banco""")
cargo = float(input("cargo: "))
salario = float(input("salario: "))

if cargo == 1:
    salario = salario * 0.30
    print ("")
