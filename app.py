estoque = [
    {"id": 1, "produto": "Mouse Gamer", "categoria": "Periféricos", "preco": 120.00,
        "quantidade": 35, "fornecedor": "Logitech", "estoque_minimo": 10},
    {"id": 2, "produto": "Teclado Mecânico", "categoria": "Periféricos",
        "preco": 250.00, "quantidade": 20, "fornecedor": "Redragon", "estoque_minimo": 5},
    {"id": 3, "produto": "Monitor 24\"", "categoria": "Monitores", "preco": 890.00,
        "quantidade": 12, "fornecedor": "Samsung", "estoque_minimo": 3},
    {"id": 4, "produto": "HD 1TB", "categoria": "Armazenamento", "preco": 300.00,
        "quantidade": 40, "fornecedor": "Seagate", "estoque_minimo": 10},
    {"id": 5, "produto": "SSD 500GB", "categoria": "Armazenamento", "preco": 450.00,
        "quantidade": 25, "fornecedor": "Kingston", "estoque_minimo": 7},
    {"id": 6, "produto": "Placa de Vídeo RTX 3060", "categoria": "Componentes",
        "preco": 2500.00, "quantidade": 4, "fornecedor": "NVIDIA", "estoque_minimo": 2},
    {"id": 7, "produto": "Processador Ryzen 5", "categoria": "Componentes",
        "preco": 1200.00, "quantidade": 10, "fornecedor": "AMD", "estoque_minimo": 3},
    {"id": 8, "produto": "Gabinete RGB", "categoria": "Gabinetes", "preco": 350.00,
        "quantidade": 15, "fornecedor": "Gamemax", "estoque_minimo": 5},
    {"id": 9, "produto": "Fonte 650W", "categoria": "Energia", "preco": 480.00,
        "quantidade": 8, "fornecedor": "Corsair", "estoque_minimo": 4},
    {"id": 10, "produto": "Cooler CPU", "categoria": "Refrigeração", "preco": 150.00,
        "quantidade": 18, "fornecedor": "Cooler Master", "estoque_minimo": 6},
]


def main():
    print('| Iniciando o app');
    print('Carregando opções..');
    show_options();

    while True:
        optionSelected = input('Selecione a opção desejada: ');

        if (optionSelected is not None):
            if (isinstance(optionSelected, str)):
                if(
                    optionSelected == "Total de itens do estoque" or
                    optionSelected == "Valor total do estoque" or
                    optionSelected == "Produtos com estoque baixo " or
                    optionSelected == "Valor por categoria" or
                    optionSelected == "Fornecedor com maior valor em produtos"
                ):
                    break;
                else:
                    print('Opção invalida, selecione outra');
            else:
                print('Opção invalida, selecione outra')
        else:
            print('Não conseguimos entender a sua mensagem :(')

    if(optionSelected == "Total de itens do estoque"):
        pass;
    elif(optionSelected == "Valor total do estoque"):
        pass;
    elif(optionSelected == "Produtos com estoque baixo "):
        pass;
    elif(optionSelected == "Valor por categoria"):
        pass;
    elif(optionSelected == "Fornecedor com maior valor em produtos"):
        pass;

def show_options():
    print(
        '|---------------------------------------|\n'
        '|Options                                |\n'
        '|---------------------------------------|\n'
        '|Total de itens do estoque              |\n'
        '|Valor total do estoque                 |\n'
        '|Produtos com estoque baixo             |\n'
        '|Valor por categoria                    |\n'
        '|Fornecedor com maior valor em produtos |\n'
        '|---------------------------------------|'
    )


# Funções auxiliares
def retirar_duplicata(arr_estoque):
    arr_no_duplicata = []
    for i in arr_estoque:
        if i not in arr_no_duplicata:
            arr_no_duplicata.append(i)
    return arr_no_duplicata

# Funções principais


def total_produtos_estoque(arr_estoque):
    return sum(item['quantidade'] for item in arr_estoque)


def total_valor_estoque(arr_estoque):
    return sum(item['preco'] * item['quantidade'] for item in arr_estoque)


def produtos_baixo_estoque(arr_estoque, quantidade_base_minima=None):
    if quantidade_base_minima is None:
        # Usa o estoque_minimo de cada produto se nenhum valor for fornecido
        return [item for item in arr_estoque if item['quantidade'] < item['estoque_minimo']]
    else:
        return [item for item in arr_estoque if item['quantidade'] < quantidade_base_minima]


def sum_by_item(name_to_filter, arr_estoque):
    items_categoria = [
        item for item in arr_estoque if item['categoria'] == name_to_filter]
    valor_total = sum(item['preco'] * item['quantidade']
                      for item in items_categoria)
    return {name_to_filter: valor_total}


def valor_by_categoria(arr_estoque):
    categorias = list(set(item['categoria'] for item in arr_estoque))
    return [sum_by_item(categoria, arr_estoque) for categoria in categorias]


def fornecedor_maior_valor(arr_estoque):
    # Criar um dicionário para agrupar por fornecedor
    fornecedores = {}
    for item in arr_estoque:
        fornecedor = item['fornecedor']
        valor = item['preco'] * item['quantidade']
        if fornecedor in fornecedores:
            fornecedores[fornecedor] += valor
        else:
            fornecedores[fornecedor] = valor

    # Converter para lista de dicionários e ordenar
    relacao = [{'fornecedor': k, 'valor': v} for k, v in fornecedores.items()]
    return sorted(relacao, key=lambda x: x['valor'], reverse=True)


if __name__ == '__main__':
    main()
