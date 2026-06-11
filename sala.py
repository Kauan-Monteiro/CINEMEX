import math
from config import FILEIRAS, VAGAS_POR_FILEIRA, LARGURA
from ui import cor, C, linha_dupla, linha_simples, titulo_secao


# utils de assento — converter string pra indice e vice-versa

def label_assento(fileira, idx):
    # ('A', 2) vira 'A3'
    return f"{fileira}{idx + 1}"

def converter_assento(s):
    # transforma 'B4' em (fileira='B', idx=3)
    # retorna (None, None) se vier coisa estranha
    try:
        s = s.strip().upper()
        fileira = s[0]
        numero  = int(s[1:]) - 1
        if fileira in FILEIRAS and 0 <= numero < VAGAS_POR_FILEIRA:
            return fileira, numero
    except Exception:
        pass
    return None, None

def recomendar_proximos(sala, f_alvo, n_alvo, qtd=3):
    # busca os assentos livres mais perto do que o usuario queria
    # usa distancia euclidiana simples, funciona bem pra esse caso
    idx_f      = FILEIRAS.index(f_alvo)
    candidatos = []
    for fi, fileira in enumerate(FILEIRAS):
        for ni in range(VAGAS_POR_FILEIRA):
            if sala[fileira][ni] == 0:
                dist = math.sqrt((fi - idx_f) ** 2 + (ni - n_alvo) ** 2)
                candidatos.append((label_assento(fileira, ni), dist))
    candidatos.sort(key=lambda x: x[1])
    return [c[0] for c in candidatos[:qtd]]


# mapa visual da sala

def exibir_sala(sala, destacar=None):
    # destacar recebe (fileira, idx) pra marcar o assento escolhido
    LIVRE   = cor("o", C["GREEN"], C["BOLD"])
    OCUPADO = cor("x", C["RED"])
    DEST    = cor("O", C["YELLOW"], C["BOLD"])

    print()
    linha_dupla()
    titulo_secao("MAPA DA SALA")
    linha_dupla()

    # tela la na frente
    tela_w = VAGAS_POR_FILEIRA * 4 + 4
    margem = " " * ((LARGURA - tela_w) // 2 + 2)
    print()
    print(margem + cor("+" + "-" * (tela_w - 2) + "+", C["CYAN"]))
    print(margem + cor("|" + " " * ((tela_w - 8) // 2) + "  TELA  " + " " * ((tela_w - 8) // 2) + "|", C["CYAN"], C["BOLD"]))
    print(margem + cor("+" + "-" * (tela_w - 2) + "+", C["CYAN"]))

    # numeracao das colunas
    cabecalho = "     "
    for i in range(VAGAS_POR_FILEIRA):
        cabecalho += cor(f"{i+1:2d} ", C["DIM"])
    print("  " + cabecalho)
    print()

    # fileiras
    for fileira in FILEIRAS:
        linha = f"  {cor(f' {fileira} ', C['YELLOW'], C['BOLD'])} | "
        for idx, status in enumerate(sala[fileira]):
            if destacar and destacar == (fileira, idx):
                linha += DEST + "  "
            elif status == 0:
                linha += LIVRE + "  "
            else:
                linha += OCUPADO + "  "
        print(linha)

    print()
    linha_simples()

    # resumo embaixo
    livres   = sum(s == 0 for f in FILEIRAS for s in sala[f])
    ocupados = VAGAS_POR_FILEIRA * len(FILEIRAS) - livres

    print(f"  {LIVRE} Livre  {OCUPADO} Ocupado  {DEST} Selecionado")
    print()
    print(f"  {cor('Disponiveis:', C['GREEN'])} {cor(str(livres), C['GREEN'], C['BOLD'])}   "
          f"{cor('Ocupados:', C['RED'])} {cor(str(ocupados), C['RED'], C['BOLD'])}   "
          f"{cor('Total:', C['DIM'])} {cor(str(VAGAS_POR_FILEIRA * len(FILEIRAS)), C['DIM'])}")
    linha_dupla()
    print()
