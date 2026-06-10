from config  import FILMES, HORARIOS
from ui      import (cor, C, limpar, pausar, digitar_animado,
                     exibir_logo, linha_dupla, titulo_secao,
                     msg_aviso, msg_erro, msg_ok)
from reservas import (selecionar_sessao, escolher_assento, checkout,
                      trocar_assento, cancelar_reserva)
from storage  import carregar_sala
from sala     import exibir_sala

# ══════════════════════════════════════════════════════════════════
#  MENU PRINCIPAL
# ══════════════════════════════════════════════════════════════════

def menu():
    filme_id   = None
    horario_id = None

    while True:
        limpar()
        exibir_logo()
        linha_dupla()
        titulo_secao("MENU PRINCIPAL")
        linha_dupla()
        print()

        if filme_id and horario_id:
            filme = FILMES[filme_id]
            print(f"  {cor('Sessão ativa:', C['DIM'])} "
                  f"{cor(filme['titulo'], C['WHITE'], C['BOLD'])}  "
                  f"{cor('·', C['DIM'])}  {cor(HORARIOS[horario_id], C['CYAN'])}")
        else:
            msg_aviso("Nenhuma sessão selecionada.")

        print()
        print(f"  {cor('[1]', C['GOLD'], C['BOLD'])}  🎬  Selecionar Filme e Horário")
        print(f"  {cor('[2]', C['GOLD'], C['BOLD'])}  🪑  Ver Mapa de Assentos")
        print(f"  {cor('[3]', C['GOLD'], C['BOLD'])}  🎟️   Reservar Assento")
        print(f"  {cor('[4]', C['GOLD'], C['BOLD'])}  🔁  Trocar de Assento")
        print(f"  {cor('[5]', C['GOLD'], C['BOLD'])}  ❌  Cancelar Reserva")
        print(f"  {cor('[0]', C['RED']            )}  🚪  Sair")
        print()
        linha_dupla()

        opcao = input(cor("  Escolha uma opção: ", C["YELLOW"])).strip()

        if opcao == "1":
            f, h = selecionar_sessao()
            if f and h:
                filme_id, horario_id = f, h
                msg_ok(f"Sessão selecionada: {FILMES[filme_id]['titulo']} às {HORARIOS[horario_id]}")
                pausar()

        elif opcao in ("2", "3", "4", "5") and not (filme_id and horario_id):
            msg_aviso("Selecione uma sessão primeiro (opção 1).")
            pausar()

        elif opcao == "2":
            limpar()
            exibir_logo()
            sala = carregar_sala(filme_id, horario_id)
            print(f"  {cor(FILMES[filme_id]['titulo'], C['WHITE'], C['BOLD'])}  "
                  f"{cor('·', C['DIM'])}  {cor(HORARIOS[horario_id], C['CYAN'])}\n")
            exibir_sala(sala)
            pausar()

        elif opcao == "3":
            resultado = escolher_assento(filme_id, horario_id)
            if resultado:
                fileira, num = resultado
                checkout(filme_id, horario_id, fileira, num)

        elif opcao == "4":
            trocar_assento(filme_id, horario_id)

        elif opcao == "5":
            cancelar_reserva(filme_id, horario_id)

        elif opcao == "0":
            limpar()
            exibir_logo()
            print()
            digitar_animado(cor("  Obrigado por usar o CINEMEX. Bom filme! 🍿",
                                C["GOLD"], C["BOLD"]))
            print()
            break

        else:
            msg_erro("Opção inválida. Tente novamente.")
            pausar()


if __name__ == "__main__":
    menu()
