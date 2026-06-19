'''
4. Suponha que o professor Fábio possui 2 logins na rede acadê-
mica da instituição. Construa um programa que valide o acesso 
do professor à rede. Caso o par usuário/senha informado esteja 
correto, o programa deve imprimir a mensagem “Seja bem vindo!”. 
Caso contrário, “Usuário e senha não conferem”.
    login 1                 login 2
    usuário: procopio       usuário: paiva 
    senha: 12345            senha: 54321
'''

senha = input("digite a senha: ")
usuario = input("usuario: ")
 
if  senha == "12345" and usuario == "procopio":
    print("seja bem vindo, procopio")
elif senha == "54321" and usuario == "paiva":
    print ("seja bem vindo, paiva")
else:
    print ("acesso negado!")


