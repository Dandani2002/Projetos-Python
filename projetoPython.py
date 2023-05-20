contagem = 0
tentrest = 3

senha = str(input("Cadastre sua senha: "))

while contagem < 3:
    asenha = str(input("Digite sua senha: "))
    if(senha == asenha):
        print("Bem Vindo, Usuário!")
        break
    else:
        print(f"Tente novamente, {tentrest} tentativas restantes ")
        contagem += 1
        tentrest -= 1
        continue
    
if (tentrest == 0):
    print("Acesso negado, Tente outro dia")
