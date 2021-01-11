def existe_contato(lista, email):

    if len(lista) > 0:
        for contato in lista:
            if contato ["email"] == email:
                return True

    return False

def adicionar(lista):


    while True:
        email = input('Digite o e-mail do contato:')

        if not existe_contato(lista, email):
            break
        else:
            print('Esse e-mail já foi utilizado') 
            print('por favor utilize outro e-mail.')


    contato = {
        'email':  (input('Digite o email: ')),
        'nome':  (input('Digite o nome: ')),
        'tel': int(input('Digite o telefone: '))
    }

    lista.append(contato)

    print('O contato {} foi cadastrado com sucesso!\n'.format(contato['nome']))



def alterar():
    pass



def excluir():
    pass



def buscar():
    pass



def listar():
    pass



def principal():

    lista = [] # Inicializando a lista vazia


    while True:
        print('1 - adicionar contato')
        print('2 - alterar contato')
        print('3 - excluir contato')
        print('4 - buscar contato')
        print('5 - listar contatos')
        print('6 - sair')
        
        opção = int(input('> '))
    
        if opção == 1:
            adicionar(lista)
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