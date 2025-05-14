import os
import time
from dataclasses import dataclass
os.system("cls || clear")

def limpar():
    os.system("cls || clear")

lista_funcionario = []

@dataclass
class Funcionario:
    nome: str
    cpf: int
    cargo: str
    salario: float

def cadastrar_funcionario(lista_funcionario): 
    funcionario = Funcionario( 
        nome = input("\nDigite o nome que deseja adicionar: "),
        cpf = int(input("Digite o cpf do funcionário que deseja adicionar: ")),
        cargo = input("Informe o cargo do funcionário: "),
        salario = float(input("Digite o salário do funcionário: ")),
    )
    print(f"\nFuncionário '{funcionario.nome}' adicionado com sucesso.")
    lista_funcionario.append(funcionario)

def listar_funcionarios(lista_funcionario):
    if not lista_funcionario:
        print("\nNão há funcionários cadastrados.")
    else:
        print(f"\n- Lista de Funcionários -")
        for funcionario in lista_funcionario:
            print(f"\nNome: {funcionario.nome}\nCPF: {funcionario.cpf}\nCargo: {funcionario.cargo}\nSalário: {funcionario.salario}\n")

def excluir_funcionario(lista_funcionario):
    listar_funcionarios(lista_funcionario)
    nome_remove = input(f"\nDigite o nome do funcionário que deseja remover: ")
    for funcionario in lista_funcionario:
        if funcionario.nome == nome_remove:  
            lista_funcionario.remove(funcionario)
            print(f"O funcionário '{nome_remove}' foi removido com sucesso.")
            return
    print(f"O funcionário {nome_remove} não foi encontrado.")

def salvar_dados(lista_funcionario):
    nome_arquivo = "Funcionarios.csv"
    
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo_usuario:
        for funcionario in lista_funcionario:
            arquivo_usuario.write(f"Nome do funcionário: {funcionario.nome}\n")
            arquivo_usuario.write(f"CPF: {funcionario.cpf}\n")
            arquivo_usuario.write(f"Cargo: {funcionario.cargo}\n")
            arquivo_usuario.write(f"Salário: {funcionario.salario}\n")

    print("\nDados salvos com sucesso!")

def carregar_dados(lista_funcionario):
    nome_arquivo = "Funcionarios.txt"
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                print(f"{linha.strip()}")
    except FileNotFoundError:
        print("Arquivo não encontrado")

def atualizar_funcionario(lista_funcionario):
    listar_funcionarios(lista_funcionario)
    nome_antigo = input(f"\nDigite o nome do funcionário que deseja atualizar: ")
    for funcionario in lista_funcionario:
        if funcionario.nome == nome_antigo:
            novo_nome = input(f"\nDigite o novo nome para '{nome_antigo}': ")
            funcionario.nome = novo_nome
            funcionario.cpf = int(input(f"Digite o novo CPF para '{novo_nome}': "))
            funcionario.cargo = input(f"Digite o novo cargo para '{novo_nome}': ")
            funcionario.salario = float(input(f"Digite o novo salário para '{novo_nome}': "))
            print(f"\nO funcionário '{nome_antigo}' foi atualizado com sucesso para {novo_nome}.")
            return
    print(f"\nO nome {nome_antigo} não foi encontrado.")

# Mostrando menu
while True:
    print("""
- Menu Interativo -
1- Cadastrar Funcionário 
2- Listar Funcionários
3- Atualizar Funcionários 
4- Excluir Funcionário
5- Salvar Dados
6- Carregar Dados 
7- Sair
""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            cadastrar_funcionario(lista_funcionario)
        case 2:
            listar_funcionarios(lista_funcionario)
        case 3:
            atualizar_funcionario(lista_funcionario)
        case 4:
            excluir_funcionario(lista_funcionario)
        case 5:
            salvar_dados(lista_funcionario)
        case 6:
            carregar_dados(lista_funcionario)
        case 7:
            os.system("cls || clear")
            print(f"\nObrigado por utilizar o sistema da empresa DENDÊ TECH !")
            break
        case _:
            print("Opção inválida.")
    
    if opcao != 1:
        time.sleep(6)
    os.system("cls || clear")
