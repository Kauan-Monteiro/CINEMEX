import os
import sys
import time

# ══════════════════════════════════════════════════════════════════
#  CORES ANSI
# ══════════════════════════════════════════════════════════════════
C = {
    "RESET":    "\033[0m",
    "BOLD":     "\033[1m",
    "DIM":      "\033[2m",
    "RED":      "\033[91m",
    "GREEN":    "\033[92m",
    "YELLOW":   "\033[93m",
    "BLUE":     "\033[94m",
    "MAGENTA":  "\033[95m",
    "CYAN":     "\033[96m",
    "WHITE":    "\033[97m",
    "BG_RED":   "\033[41m",
    "BG_GREEN": "\033[42m",
    "BG_BLUE":  "\033[44m",
    "BG_CYAN":  "\033[46m",
    "BG_DARK":  "\033[40m",
    "ORANGE":   "\033[38;5;214m",
    "GOLD":     "\033[38;5;220m",
    "PURPLE":   "\033[38;5;135m",
    "DARK_RED": "\033[38;5;160m",
}

def cor(texto, *estilos):
    return "".join(estilos) + texto + C["RESET"]

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def pausar(msg="  Pressione ENTER para continuar..."):
    print()
    input(cor(msg, C["DIM"]))

def digitar_animado(texto, delay=0.018):
    for ch in texto:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ══════════════════════════════════════════════════════════════════
#  MENSAGENS
# ══════════════════════════════════════════════════════════════════
def msg_ok(texto):
    print(f"\n  {cor('✔', C['GREEN'], C['BOLD'])}  {cor(texto, C['GREEN'])}")

def msg_erro(texto):
    print(f"\n  {cor('✘', C['RED'], C['BOLD'])}  {cor(texto, C['RED'])}")

def msg_info(texto):
    print(f"  {cor('ℹ', C['CYAN'])}  {cor(texto, C['CYAN'])}")

def msg_aviso(texto):
    print(f"  {cor('⚠', C['YELLOW'])}  {cor(texto, C['YELLOW'])}")

# ══════════════════════════════════════════════════════════════════
#  DIVISORES
# ══════════════════════════════════════════════════════════════════
from config import LARGURA

def linha_dupla():
    print(cor("  " + "═" * LARGURA, C["GOLD"], C["DIM"]))

def linha_simples():
    print(cor("  " + "─" * LARGURA, C["DIM"]))

def titulo_secao(texto):
    pad  = LARGURA - len(texto) - 4
    esq  = pad // 2
    dir_ = pad - esq
    print(cor(f"  ╠{'═'*esq}[ ", C["GOLD"], C["DIM"]) +
          cor(texto, C["WHITE"], C["BOLD"]) +
          cor(f" ]{'═'*dir_}╣", C["GOLD"], C["DIM"]))

# ══════════════════════════════════════════════════════════════════
#  LOGO
# ══════════════════════════════════════════════════════════════════
def exibir_logo():
    linhas = [
        "",
        cor("  ╔═══════════════════════════════════════════════════════════╗", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("   ██████╗██╗███╗   ██╗███████╗███╗   ███╗███████╗██╗  ██╗  ", C["ORANGE"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("  ██╔════╝██║████╗  ██║██╔════╝████╗ ████║██╔════╝╚██╗██╔╝  ", C["ORANGE"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("  ██║     ██║██╔██╗ ██║█████╗  ██╔████╔██║█████╗   ╚███╔╝   ", C["GOLD"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("  ██║     ██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══╝   ██╔██╗   ", C["ORANGE"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("  ╚██████╗██║██║ ╚████║███████╗██║ ╚═╝ ██║███████╗██╔╝ ██╗  ", C["DARK_RED"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("   ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝  ", C["DARK_RED"], C["BOLD"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ║", C["GOLD"], C["BOLD"]) +
        cor("              🎬  O CINEMA QUE VOCÊ MERECE  🎬               ", C["YELLOW"]) +
        cor("║", C["GOLD"], C["BOLD"]),
        cor("  ╚═══════════════════════════════════════════════════════════╝", C["GOLD"], C["BOLD"]),
        "",
    ]
    for l in linhas:
        print(l)
