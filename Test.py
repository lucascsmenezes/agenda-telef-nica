def principal():

def adicionar():
    pass

def alterar():
    pass

def excluir():
    pass

def buscar():
    pass

def listar():
    pass

def sair():
    pass

    while True:
        print('1 - adicionar contato')
        print('2 - alterar contato')
        print('3 - excluir contato')
        print('4 - buscar contato')
        print('5 - listar contatos')
        print('6 - sair')
        opção = int(input('> '))
    
        if opção == 1:
            adicionar()
        elif opção == 2:
            alterar()
        elif opção == 3:
            excluir
        elif opção == 4:
            buscar()
        elif opção == 5:
            listar()
        elif  opção == 6:
            print('Saindo do programa...')
            break
        else:
            print('Opção Invalida')


principal()
