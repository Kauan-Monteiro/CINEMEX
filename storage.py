import os
from config import DATA_DIR, FILEIRAS, VAGAS_POR_FILEIRA

# persistencia em arquivo .txt
#
# formato: sala_<filme_id>_<horario_id>.txt
# cada linha e uma fileira:
#   A:0000000000
#   B:0010100000
# 0 = livre, 1 = ocupado — simples e funciona


def _garantir_data_dir():
    # cria a pasta de dados se nao existir ainda
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def _caminho_sala(filme_id, horario_id):
    return os.path.join(DATA_DIR, f"sala_{filme_id}_{horario_id}.txt")

def inicializar_sala():
    # sala zerada, tudo livre
    return {f: [0] * VAGAS_POR_FILEIRA for f in FILEIRAS}

def carregar_sala(filme_id, horario_id):
    # le o arquivo e monta o dict; se nao existir ainda, devolve sala vazia
    _garantir_data_dir()
    caminho = _caminho_sala(filme_id, horario_id)

    if not os.path.exists(caminho):
        return inicializar_sala()

    sala = inicializar_sala()
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha or ":" not in linha:
                    continue
                fileira, assentos = linha.split(":", 1)
                fileira = fileira.strip().upper()
                if fileira in FILEIRAS and len(assentos) == VAGAS_POR_FILEIRA:
                    sala[fileira] = [int(c) for c in assentos]
    except (ValueError, IOError):
        # arquivo corrompido ou ilegivel — começa do zero
        return inicializar_sala()

    return sala

def salvar_sala(filme_id, horario_id, sala):
    # grava cada fileira como uma linha no arquivo
    _garantir_data_dir()
    caminho = _caminho_sala(filme_id, horario_id)

    with open(caminho, "w", encoding="utf-8") as f:
        for fileira in FILEIRAS:
            assentos = "".join(str(v) for v in sala[fileira])
            f.write(f"{fileira}:{assentos}\n")
