# configurações gerais do sistema
# mexe aqui se precisar mudar fileiras, vagas ou largura do terminal

DATA_DIR         = "cinemex_data"
FILEIRAS         = ['A', 'B', 'C', 'D', 'E', 'F']
VAGAS_POR_FILEIRA = 10
LARGURA          = 63

FILMES = {
    "1": {
        "titulo":  "Homem-Aranha: Um Novo Universo",
        "genero":  "Animacao / Acao",
        "duracao": "1h 57min",
        "classif": "12",
        "preco":   28.00,
        "trailer": "https://www.youtube.com/watch?v=g4Hbz2jLxvQ",
    },
    "2": {
        "titulo":  "Todo Mundo em Panico 6",
        "genero":  "Comedia / Terror",
        "duracao": "1h 42min",
        "classif": "16",
        "preco":   26.00,
        "trailer": "https://www.youtube.com/watch?v=J4QBtG-JqEY",
    },
    "3": {
        "titulo":  "Duna: Parte Dois",
        "genero":  "Ficcao Cientifica",
        "duracao": "2h 46min",
        "classif": "12",
        "preco":   32.00,
        "trailer": "https://www.youtube.com/watch?v=Way9Dexny3w",
    },
    "4": {
        "titulo":  "Deadpool & Wolverine",
        "genero":  "Acao / Comedia",
        "duracao": "2h 07min",
        "classif": "18",
        "preco":   34.00,
        "trailer": "https://www.youtube.com/watch?v=73_1biulkYk",
    },
    "5": {
        "titulo":  "Divertida Mente 2",
        "genero":  "Animacao / Aventura",
        "duracao": "1h 40min",
        "classif": "L",
        "preco":   28.00,
        "trailer": "https://www.youtube.com/watch?v=LEjhY15eCx0",
    },
}

HORARIOS = {
    "1": "13:30",
    "2": "16:00",
    "3": "19:15",
    "4": "22:00",
}

FORMAS_PAGAMENTO = {
    "1": ("Cartao de Credito", "parcelamos em ate 3x sem juros"),
    "2": ("Cartao de Debito",  "pagamento imediato"),
    "3": ("PIX",              "desconto adicional de R$ 2,00"),
    "4": ("Dinheiro",         "troco disponivel"),
}
