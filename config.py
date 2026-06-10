# ══════════════════════════════════════════════════════════════════
#  CONFIGURAÇÕES GLOBAIS
# ══════════════════════════════════════════════════════════════════

DATA_DIR         = "cinemex_data"
FILEIRAS         = ['A', 'B', 'C', 'D', 'E', 'F']
VAGAS_POR_FILEIRA = 10
LARGURA          = 63

FILMES = {
    "1": {
        "titulo":  "Homem-Aranha: Um Novo Universo",
        "genero":  "Animação / Ação",
        "duracao": "1h 57min",
        "classif": "12",
        "preco":   28.00,
        "trailer": "https://www.youtube.com/watch?v=g4Hbz2jLxvQ",
        "emoji":   "🕷️",
    },
    "2": {
        "titulo":  "Todo Mundo em Pânico 6",
        "genero":  "Comédia / Terror",
        "duracao": "1h 42min",
        "classif": "16",
        "preco":   26.00,
        "trailer": "https://www.youtube.com/watch?v=J4QBtG-JqEY",
        "emoji":   "😱",
    },
    "3": {
        "titulo":  "Duna: Parte Dois",
        "genero":  "Ficção Científica",
        "duracao": "2h 46min",
        "classif": "12",
        "preco":   32.00,
        "trailer": "https://www.youtube.com/watch?v=Way9Dexny3w",
        "emoji":   "🏜️",
    },
    "4": {
        "titulo":  "Deadpool & Wolverine",
        "genero":  "Ação / Comédia",
        "duracao": "2h 07min",
        "classif": "18",
        "preco":   34.00,
        "trailer": "https://www.youtube.com/watch?v=73_1biulkYk",
        "emoji":   "⚔️",
    },
    "5": {
        "titulo":  "Divertida Mente 2",
        "genero":  "Animação / Aventura",
        "duracao": "1h 40min",
        "classif": "L",
        "preco":   28.00,
        "trailer": "https://www.youtube.com/watch?v=LEjhY15eCx0",
        "emoji":   "🎭",
    },
}

HORARIOS = {
    "1": "13:30",
    "2": "16:00",
    "3": "19:15",
    "4": "22:00",
}

FORMAS_PAGAMENTO = {
    "1": ("💳  Cartão de Crédito", "Parcelamos em até 3x sem juros"),
    "2": ("💳  Cartão de Débito",  "Pagamento imediato"),
    "3": ("📱  PIX",              "Desconto adicional de R$ 2,00"),
    "4": ("💵  Dinheiro",         "Troco disponível"),
}
