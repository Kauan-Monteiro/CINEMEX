import os
from config import DATA_DIR, FILEIRAS, VAGAS_POR_FILEIRA

# ══════════════════════════════════════════════════════════════════
#  PERSISTÊNCIA EM ARQUIVO .TXT
#
#  Formato do arquivo sala_<filme_id>_<horario_id>.txt:
#
#  Cada linha representa uma fileira:
#    A:0000000000
#    B:0010100000
#    ...
#
#  0 = livre, 1 = ocupado
# ══════════════════════════════════════════════════════════════════

def _garantir_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def _caminho_sala(filme_id, horario_id):
    return os.path.join(DATA_DIR, f"sala_{filme_id}_{horario_id}.txt")

def inicializar_sala():
    """Retorna sala vazia: dict[fileira] = lista de 0s."""
    return {f: [0] * VAGAS_POR_FILEIRA for f in FILEIRAS}

def carregar_sala(filme_id, horario_id):
    """Lê o arquivo .txt e devolve o dicionário da sala."""
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
        return inicializar_sala()

    return sala

def salvar_sala(filme_id, horario_id, sala):
    """Grava o dicionário da sala no arquivo .txt."""
    _garantir_data_dir()
    caminho = _caminho_sala(filme_id, horario_id)

    with open(caminho, "w", encoding="utf-8") as f:
        for fileira in FILEIRAS:
            assentos = "".join(str(v) for v in sala[fileira])
            f.write(f"{fileira}:{assentos}\n")
