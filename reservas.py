import webbrowser
from datetime import datetime

from config  import FILMES, HORARIOS, FORMAS_PAGAMENTO
from ui      import (cor, C, limpar, pausar, digitar_animado,
                     exibir_logo, linha_dupla, linha_simples,
                     titulo_secao, msg_ok, msg_erro, msg_info, msg_aviso)
from storage import carregar_sala, salvar_sala
from sala    import exibir_sala, converter_assento, label_assento, recomendar_proximos

# ══════════════════════════════════════════════════════════════════
#  SELEÇÃO DE SESSÃO
# ══════════════════════════════════════════════════════════════════

def selecionar_sessao():
    """Exibe filmes e horários; retorna (filme_id, horario_id) ou (None, None)."""
    limpar()
    exibir_logo()
    linha_dupla()
    titulo_secao("FILMES EM CARTAZ")
    linha_dupla()
    print()

    for k, f in FILMES.items():
        classif_cor = (C["GREEN"]  if f["classif"] in ("L", "12")
                  else C["YELLOW"] if f["classif"] == "16"
                  else C["RED"])
        preco_str = f"R$ {f['preco']:.2f}"
        print(f"  {cor(f'[{k}]', C['GOLD'], C['BOLD'])}  {f['emoji']}  "
              f"{cor(f['titulo'], C['WHITE'], C['BOLD'])}")
        print(f"       {cor(f['genero'], C['CYAN'])}  ·  {cor(f['duracao'], C['DIM'])}  ·  "
              f"Classif. {cor(f['classif'], classif_cor, C['BOLD'])}  ·  "
              f"{cor(preco_str, C['GOLD'])}")
        linha_simples()

    print()
    filme_id = input(cor("  Escolha o número do filme: ", C["YELLOW"])).strip()
    if filme_id not in FILMES:
        msg_erro("Filme inválido.")
        pausar()
        return None, None

    limpar()
    exibir_logo()
    linha_dupla()
    titulo_secao(f"HORÁRIOS — {FILMES[filme_id]['titulo']}")
    linha_dupla()
    print()
    hoje = datetime.now().strftime("%d/%m/%Y")
    print(f"  {cor('Data:', C['DIM'])} {cor(hoje, C['WHITE'])}\n")

    for k, h in HORARIOS.items():
        sala_tmp = carregar_sala(filme_id, k)
        livres   = sum(s == 0 for f in FILMES for s in sala_tmp.get(f, []))
        # contagem correta percorrendo todas as fileiras
        livres = sum(sala_tmp[fila][i] == 0
                     for fila in sala_tmp
                     for i in range(len(sala_tmp[fila])))
        print(f"  {cor(f'[{k}]', C['GOLD'], C['BOLD'])}  🕐 {cor(h, C['WHITE'], C['BOLD'])}  "
              f"─  {cor(f'{livres} assentos disponíveis', C['GREEN'] if livres > 5 else C['YELLOW'])}")

    print()
    horario_id = input(cor("  Escolha o horário: ", C["YELLOW"])).strip()
    if horario_id not in HORARIOS:
        msg_erro("Horário inválido.")
        pausar()
        return None, None

    return filme_id, horario_id

# ══════════════════════════════════════════════════════════════════
#  ESCOLHA DE ASSENTO
# ══════════════════════════════════════════════════════════════════

def escolher_assento(filme_id, horario_id):
    """Loop de seleção de assento. Retorna (fileira, idx) ou None."""
    while True:
        sala = carregar_sala(filme_id, horario_id)
        limpar()
        exibir_logo()
        print(f"  {cor(FILMES[filme_id]['titulo'], C['WHITE'], C['BOLD'])}  "
              f"{cor('·', C['DIM'])}  {cor(HORARIOS[horario_id], C['CYAN'])}\n")
        exibir_sala(sala)

        print(cor("  Digite o assento desejado (ex: A3, C7) ou [0] para voltar:", C["YELLOW"]))
        entrada = input(cor("  >> ", C["GOLD"], C["BOLD"])).strip()

        if entrada == "0":
            return None

        fileira, num = converter_assento(entrada)

        if not fileira:
            msg_erro("Formato inválido. Use letra + número (ex: B4).")
            pausar("  Pressione ENTER para tentar novamente...")
            continue

        if sala[fileira][num] == 1:
            msg_erro(f"O assento {label_assento(fileira, num)} está ocupado.")
            proximos = recomendar_proximos(sala, fileira, num)
            if proximos:
                msg_info(f"Assentos próximos disponíveis: "
                         f"{cor(', '.join(proximos), C['CYAN'], C['BOLD'])}")
                escolha = input(cor("  Selecione um dos sugeridos ou outro assento: ",
                                    C["YELLOW"])).strip()
                if escolha.strip().upper() == "0":
                    return None
                f2, n2 = converter_assento(escolha)
                if f2 and sala[f2][n2] == 0:
                    return f2, n2
                msg_erro("Assento inválido ou ocupado.")
                pausar()
            else:
                msg_aviso("Não há assentos disponíveis na sala.")
                pausar()
            continue

        # Pré-visualização com destaque
        limpar()
        exibir_logo()
        exibir_sala(sala, destacar=(fileira, num))
        msg_ok(f"Assento {cor(label_assento(fileira, num), C['YELLOW'], C['BOLD'])} selecionado!")
        resp = input(cor("  Confirmar este assento? [S/N]: ", C["YELLOW"])).strip().upper()
        if resp == "S":
            return fileira, num

# ══════════════════════════════════════════════════════════════════
#  CHECKOUT / PAGAMENTO
# ══════════════════════════════════════════════════════════════════

def checkout(filme_id, horario_id, fileira, num):
    """Exibe resumo, aplica descontos, registra reserva. Retorna True se confirmado."""
    filme      = FILMES[filme_id]
    preco_base = filme["preco"]

    limpar()
    exibir_logo()
    linha_dupla()
    titulo_secao("RESUMO DA RESERVA")
    linha_dupla()
    print()
    print(f"  {cor('Filme:', C['DIM'])}   {cor(filme['titulo'], C['WHITE'], C['BOLD'])}")
    print(f"  {cor('Horário:', C['DIM'])} {cor(HORARIOS[horario_id], C['CYAN'])}")
    print(f"  {cor('Assento:', C['DIM'])} {cor(label_assento(fileira, num), C['YELLOW'], C['BOLD'])}")
    print(f"  {cor('Valor:', C['DIM'])}   {cor(f'R$ {preco_base:.2f}', C['GOLD'], C['BOLD'])}")
    print()

    # Desconto estudante
    linha_simples()
    titulo_secao("DESCONTO ESTUDANTE")
    linha_simples()
    print()
    print(f"  Meia-entrada para estudantes: {cor('50% de desconto', C['GREEN'], C['BOLD'])}")
    msg_aviso("Apresente carteirinha válida na bilheteria.")
    print()
    eh_estudante = input(cor("  Você é estudante? [S/N]: ", C["YELLOW"])).strip().upper()
    desconto = preco_base * 0.50 if eh_estudante == "S" else 0.0
    if desconto:
        msg_ok(f"Desconto de R$ {desconto:.2f} aplicado!")

    # Forma de pagamento
    print()
    linha_simples()
    titulo_secao("FORMA DE PAGAMENTO")
    linha_simples()
    print()
    for k, (nome, detalhe) in FORMAS_PAGAMENTO.items():
        print(f"  {cor(f'[{k}]', C['GOLD'], C['BOLD'])}  {cor(nome, C['WHITE'])}  "
              f"{cor('—', C['DIM'])}  {cor(detalhe, C['DIM'])}")
    print()
    pagamento_id = input(cor("  Escolha a forma de pagamento: ", C["YELLOW"])).strip()
    if pagamento_id not in FORMAS_PAGAMENTO:
        msg_erro("Opção inválida. Cancelando.")
        pausar()
        return False

    desconto_pix = 2.00 if pagamento_id == "3" else 0.0
    if desconto_pix:
        msg_ok("Desconto PIX de R$ 2,00 aplicado!")

    preco_final = max(0, preco_base - desconto - desconto_pix)

    # Comprovante
    print()
    linha_dupla()
    titulo_secao("COMPROVANTE")
    linha_dupla()
    print()
    print(f"  {cor('Filme:', C['DIM'])}        {cor(filme['titulo'], C['WHITE'], C['BOLD'])}")
    print(f"  {cor('Horário:', C['DIM'])}      {cor(HORARIOS[horario_id], C['CYAN'])}")
    print(f"  {cor('Assento:', C['DIM'])}      {cor(label_assento(fileira, num), C['YELLOW'], C['BOLD'])}")
    linha_simples()
    print(f"  {cor('Valor base:', C['DIM'])}   R$ {preco_base:.2f}")
    if desconto:
        print(f"  {cor('Desc. estudante:', C['GREEN'])} - R$ {desconto:.2f}")
    if desconto_pix:
        print(f"  {cor('Desc. PIX:', C['GREEN'])}      - R$ {desconto_pix:.2f}")
    linha_simples()
    print(f"  {cor('TOTAL:', C['GOLD'], C['BOLD'])}        "
          f"{cor(f'R$ {preco_final:.2f}', C['GOLD'], C['BOLD'])}")
    print(f"  {cor('Pagamento:', C['DIM'])}    {FORMAS_PAGAMENTO[pagamento_id][0]}")
    print()

    confirmar = input(cor("  Confirmar compra? [S/N]: ", C["YELLOW"])).strip().upper()
    if confirmar != "S":
        msg_aviso("Compra cancelada.")
        pausar()
        return False

    # Persiste reserva
    sala = carregar_sala(filme_id, horario_id)
    sala[fileira][num] = 1
    salvar_sala(filme_id, horario_id, sala)

    print()
    digitar_animado(cor("  ✔  Reserva confirmada com sucesso!", C["GREEN"], C["BOLD"]))
    msg_info(f"Assento {label_assento(fileira, num)} — {filme['titulo']} — {HORARIOS[horario_id]}")
    print()

    linha_simples()
    ver_trailer = input(cor("  Deseja assistir ao trailer no YouTube? [S/N]: ", C["CYAN"])).strip().upper()
    if ver_trailer == "S":
        msg_info("Abrindo trailer no navegador...")
        webbrowser.open(filme["trailer"])

    pausar("\n  Pressione ENTER para voltar ao menu...")
    return True

# ══════════════════════════════════════════════════════════════════
#  TROCAR ASSENTO
# ══════════════════════════════════════════════════════════════════

def trocar_assento(filme_id, horario_id):
    sala = carregar_sala(filme_id, horario_id)
    limpar()
    exibir_logo()
    exibir_sala(sala)

    print(cor("  Informe seu assento ATUAL:", C["YELLOW"]))
    f_atual, n_atual = converter_assento(
        input(cor("  >> ", C["GOLD"], C["BOLD"])).strip()
    )

    if not f_atual or sala[f_atual][n_atual] == 0:
        msg_erro("Assento atual inválido ou não reservado.")
        pausar()
        return

    print(cor("\n  Informe o NOVO assento desejado:", C["YELLOW"]))
    f_novo, n_novo = converter_assento(
        input(cor("  >> ", C["GOLD"], C["BOLD"])).strip()
    )

    if not f_novo:
        msg_erro("Novo assento inválido.")
        pausar()
        return

    if sala[f_novo][n_novo] == 1:
        msg_erro(f"O assento {label_assento(f_novo, n_novo)} já está ocupado.")
        pausar()
        return

    sala[f_atual][n_atual] = 0
    sala[f_novo][n_novo]   = 1
    salvar_sala(filme_id, horario_id, sala)
    msg_ok(f"Troca realizada: {label_assento(f_atual, n_atual)} → {label_assento(f_novo, n_novo)}")
    pausar()

# ══════════════════════════════════════════════════════════════════
#  CANCELAR RESERVA
# ══════════════════════════════════════════════════════════════════

def cancelar_reserva(filme_id, horario_id):
    sala = carregar_sala(filme_id, horario_id)
    limpar()
    exibir_logo()
    exibir_sala(sala)

    print(cor("  Informe o assento a cancelar:", C["YELLOW"]))
    fileira, num = converter_assento(
        input(cor("  >> ", C["GOLD"], C["BOLD"])).strip()
    )

    if not fileira or sala[fileira][num] == 0:
        msg_erro("Assento inválido ou já está livre.")
        pausar()
        return

    confirmar = input(cor(
        f"  Cancelar reserva do assento {label_assento(fileira, num)}? [S/N]: ",
        C["YELLOW"]
    )).strip().upper()

    if confirmar == "S":
        sala[fileira][num] = 0
        salvar_sala(filme_id, horario_id, sala)
        msg_ok("Reserva cancelada com sucesso.")
    else:
        msg_aviso("Operação cancelada.")
    pausar()
