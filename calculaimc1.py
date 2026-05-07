#calculadora imc
print ("""
       ------------- Tabela de IMC ---------
       menor que 18.5     | magreza
       entre 18.5 e 24.9  | peso normal
       entre 25.0 e 29.9  | sobrepeso
       entre 30.0 e 39.9  | obesidade
       acima de 40        | obesidade grave
       -------------------------------------
""")

altura = float(input("Informe a altura (em metros, ex: 1.70): "))
peso = float(input("Informe o peso (em kg, ex: 71.3): "))
imc = peso/(altura**2)
print(f"O valor do IMC é: {imc:.2f}")