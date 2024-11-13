import json
import os

# Função para carregar o estoque a partir do arquivo JSON
def carregar_estoque():
    if not os.path.exists('estoque.json'):
        return {}
    with open('estoque.json', 'r') as arquivo:
        return json.load(arquivo)

# Função para salvar o estoque no arquivo JSON
def salvar_estoque(estoque):
    with open('estoque.json', 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

# Função para adicionar um produto ao estoque
def adicionar_produto(estoque):
    produto = input("Digite o nome do produto: ").strip()
    if produto in estoque:
        print(f"O produto '{produto}' já existe no estoque.")
    else:
        try:
            quantidade = int(input(f"Digite a quantidade do produto '{produto}': "))
            preco = float(input(f"Digite o preço do produto '{produto}': "))
            estoque[produto] = {'quantidade': quantidade, 'preco': preco}
            salvar_estoque(estoque)
            print(f"Produto '{produto}' adicionado com sucesso!")
        except ValueError:
            print("Entrada inválida! Por favor, insira números válidos para a quantidade e preço.")

# Função para listar todos os produtos no estoque
def listar_produtos(estoque):
    if not estoque:
        print("O estoque está vazio.")
    else:
        print("\nEstoque atual:")
        for produto, detalhes in estoque.items():
            print(f"Produto: {produto}")
            print(f"  Quantidade: {detalhes['quantidade']}")
            print(f"  Preço: R${detalhes['preco']:.2f}")
            print("-" * 30)

# Função para remover um produto do estoque
def remover_produto(estoque):
    produto = input("Digite o nome do produto a ser removido: ").strip()
    if produto in estoque:
        del estoque[produto]
        salvar_estoque(estoque)
        print(f"Produto '{produto}' removido com sucesso.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

# Função para atualizar a quantidade de um produto no estoque
def atualizar_quantidade(estoque):
    produto = input("Digite o nome do produto a ser atualizado: ").strip()
    if produto in estoque:
        try:
            nova_quantidade = int(input(f"Digite a nova quantidade para o produto '{produto}': "))
            estoque[produto]['quantidade'] = nova_quantidade
            salvar_estoque(estoque)
            print(f"A quantidade do produto '{produto}' foi atualizada para {nova_quantidade}.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido para a quantidade.")
    else:
        print(f"Produto '{produto}' não encontrado no estoque.")

# Função principal para exibir o menu e interagir com o usuário
def menu():
    estoque = carregar_estoque()
    
    while True:
        print("\nMenu de Gerenciamento de Estoque")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Atualizar Quantidade")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_produto(estoque)
        elif escolha == '2':
            listar_produtos(estoque)
        elif escolha == '3':
            remover_produto(estoque)
        elif escolha == '4':
            atualizar_quantidade(estoque)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

# Executar o programa
if __name__ == "__main__":
    menu()
