def codigo():
    num=input("Digite o código do produto:")
    while num.isdigit() == False or int(num)<0:
        print("Código inválido!")
        num=input("Digite o Código do produto:")
    return int (num)
    
def preco():
    num=input("Digite o preço do produto:")
    while  num.replace(".","",1).isdigit() == False or float(num)<0:
        print("Preço inválido!")
        num=input("Digite o preço do produto:")
    return float(num)
    
def desejaContinuar():
    letra=input("Deseja continuar? S-sim ou N-não:").upper()
    while letra!="S" and letra!="N":
        print("Letra Inválida!")
        letra=input("Deseja continuar? S-sim ou N-não:").upper()
    return letra
    
def aumento():
    alt=float(input("Digite a porcentagem de aumento que deseja aplicar:"))
    while alt<0:
        print("Porcentagem Inválida!")
        alt=float(input("Digite a porcentagem de aumento que deseja aplicar:"))
    return alt
    
def pesquisar(códigos,pesq):
    i=0
    while i<len(códigos):
        if códigos[i] == pesq:
            return i 
        else:
            i=i+1 
    return -1
    
def inserirProdutos(códigos,precos):
    continuar="S"
    while continuar=="S":
        co=codigo()
        pes=pesquisar(códigos,co) 
        if pes == -1:
            códigos.append(co)
            pe=preco()
            precos.append(pe)
            continuar=desejaContinuar()
        else:
            print("Esse código já existe!")
            
def pesquisarPorCódigo(códigos,precos):
    cod=codigo()
    pesq=pesquisar(códigos,cod)
    if pesq>=0:
        print("Código solicitado: %d"%códigos[pesq])
        print("Preço referente ao código:%.2f R$"%precos[pesq])
    else:
        print("Código não encontrado!")
        
def aumentarPreco(códigos,precos):
    codi=codigo()
    pesqu=pesquisar(códigos,codi)
    if pesqu>=0:
        p=aumento()
        precos[pesqu]=precos[pesqu]+(precos[pesqu]*(p/100))
        print("Código do produto:%d"%códigos[pesqu])
        print("Preço atualizado:%.2f R$"%precos[pesqu])
    else:
        print("Produto não encontrado!")
        
def maiorPreco(códigos,precos):
    if len(precos) == 0:
        print("Nenhum produto cadastrado.")
    else:
        maior_preco = precos[0]
        indice_maior_preco = 0
        i = 1
        while i < len(precos):
            if precos[i] > maior_preco:
                maior_preco = precos[i]
                indice_maior_preco = i
            i= i+1
        print("Código do produto com maior preço:%d"%códigos[indice_maior_preco])
        print("Preço do produto:%.2f R$"%maior_preco)
            
def imprimir(códigos,precos):
    i=0
    print("Código \t Preço(R$) \t")
    while i<len(códigos):
        if códigos[i]>=0:
            print("%2d \t %.2f"%(códigos[i],precos[i]))
        i=i+1
        
def excluir(códigos,precos):
    codic=codigo()
    pesqui=pesquisar(códigos,codic)
    if pesqui>=0:
        del(códigos[pesqui])
        del(precos[pesqui])
    else:
        print("Código não encontrado!")
        
def menu() :
    op = ""
    while op.isdigit() == False or int(op) < 0 or int(op) > 6:
        
        print("\n" * 130)        
        print("SISTEMA DE ESTOQUE")
        print("1-Inserir")
        print("2-Pesquisar")
        print("3-Atualizar")
        print("4-Maior")
        print("5-Excluir")
        print("6-Listar")
        print("0-Sair")
        op = input("Escolha sua opção: ")
    return int(op)

###### PROGRAMA PRINCIPAL ##########
def main():
    códigos=[]
    precos=[]
    op = 1
    while op != 0:
        op = menu()
        
        if op == 0:
            print("\n\nFim do programa!!!\n\n")
            
        elif op == 1:
            print("\nCAMPO PARA INSERIR O CÓDIGO E PREÇO DOS PRODUTOS (NÃO PODE HAVER CÓDIGO REPETIDO!)\n")
            inserirProdutos(códigos,precos)
            
        elif op == 2:
            print("\nPESQUISE PELO CÓDIGO DO PRODUTO PARA SABER SEU RESPECTIVO PREÇO\n")
            pesquisarPorCódigo(códigos,precos)

        elif op == 3:
            print("\nPESQUISE PELO CÓDIGO DO PRODUTO E APLIQUE O AUMENTO QUE DESEJAR\n")
            aumentarPreco(códigos,precos)

        elif op == 4:
            print("\nCÓDIGO COM MAIOR PREÇO\n")
            maiorPreco(códigos,precos)

        elif op == 5:
            print("\nCAMPO PARA EXCLUIR PRODUTO ATRAVÉS DO CÓDIGO\n")
            excluir(códigos,precos)

        elif op == 6:
            imprimir(códigos,precos)
        
        else:
            print("Opção inválida!")

        input("Pressione <enter> para continuar ...")
    
main()