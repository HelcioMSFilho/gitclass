import os

# Lista
# #restaurantes = ['Pizza Hut', 'McDonalds', 'Subway']

# Dicionario
restaurantes = [{'nome':'Pizza Hut', 'categoria':'Pizzas', 'ativo':True}, 
                {'nome':'McDonalds', 'categoria':'Fast Food', 'ativo':False}, 
                {'nome':'Subway', 'categoria':'Sanduíches', 'ativo':True}]

def exibir_nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
\n""")

def exibir_opcoes():
    print('1 - Cadastrar Restaurante')
    print('2 - Listar Restaurantes')
    print('3 - Ativar/Desativar Restaurante')
    print('4 - Sair')

def escolher_opcao():
    try:
        # Padrao de variáveis: snake_case
        input_option = int(input('Escolha uma opção: '))
        print(f'Opção escolhida: {input_option}')
        match input_option:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_desativar_restaurante()
            case 4:
                finalizar_app()
            case _:
                opca_invalida()
    except:
        opca_invalida()

def listar_restaurantes():
    inicia_menu('Cadastrar Restaurante')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado.')
    else:
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria_restaurante = restaurante['categoria']
            ativo_restaurante = 'Ativo' if restaurante['ativo'] else 'Inativo'
            print(f'Nome: {nome_restaurante.ljust(10)} | Categoria: {categoria_restaurante.ljust(10)} | Status: {ativo_restaurante.ljust(10)}')
            
    voltar_ao_menu()

def cadastrar_novo_restaurante():
    '''
    Cadastra um novo restaurante
    Inputs:
        - nome_restaurante: str
        - categoria: str
    Outputs:
        - Adiciona o restaurante na lista de restaurantes
    '''
    inicia_menu('Cadastrar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante:\n')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}:\n')
    dados_do_resturante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_resturante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')
    voltar_ao_menu()

def ativar_desativar_restaurante():
    inicia_menu('Ativar Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o stado:\n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'].lower() == nome_restaurante.lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'Restaurante {restaurante["nome"]} foi {status}.')
            break
    if not restaurante_encontrado:
        print(f'Restaurante {nome_restaurante} não encontrado.')
    
    voltar_ao_menu()

def opca_invalida():
    print('Opção inválida. Digite um número inteiro.')
    voltar_ao_menu()

def inicia_menu(mensagem):
    os.system('clear')
    linha = '*' * (len(mensagem) + 4)
    print(f'{linha}\n* {mensagem} *\n{linha}')

def voltar_ao_menu():
    input('\nPressione uma tecla para voltar ao menu principal ')
    main()

def finalizar_app():
    inicia_menu('Finalizando App')

def main():
    os.system('clear')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
