import random
import string
import time

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.text import Text
from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn


console = Console()


def gerar_codigo_secreto(quant_caracteres):
    caracteres = string.ascii_uppercase + string.digits
    pool = random.sample(caracteres, quant_caracteres)
    codigo_secreto = "".join(random.sample(pool, quant_caracteres))
    return pool, codigo_secreto


def tela_inicial():
    console.clear()

    titulo = Text("BRUTE FORCE", style="bold bright_magenta")
    subtitulo = Text("Sistema de quebra de senha iniciado...", style="bright_cyan")

    console.print(
        Panel.fit(
            f"{titulo}\n{subtitulo}",
            border_style="bright_cyan",
            title="[bold bright_magenta]TERMINAL HACKER[/bold bright_magenta]"
        )
    )

    with Progress(
        TextColumn("[bold bright_cyan]Invadindo sistema...[/bold bright_cyan]"),
        BarColumn(
            bar_width=45,
            style="magenta",
            complete_style="bright_cyan",
            finished_style="bright_green"
        ),
        TextColumn("[bold bright_magenta]{task.percentage:>3.0f}%[/bold bright_magenta]"),
        TimeElapsedColumn(),
        console=console
    ) as progress:

        tarefa = progress.add_task("carregando", total=25)

        while not progress.finished:
            progress.update(tarefa, advance=1)
            time.sleep(0.03)


def mostrar_menu():
    table = Table(
        title="[bold bright_magenta]MENU DE INFILTRAÇÃO[/bold bright_magenta]",
        border_style="bright_cyan"
    )

    table.add_column("Opção", style="bold bright_cyan", justify="center")
    table.add_column("Nível", style="bold bright_magenta")
    table.add_column("Descrição", style="white")

    table.add_row("1", "Nível 1", "Senha com 3 caracteres")
    table.add_row("2", "Nível 2", "Senha com 4 caracteres")
    table.add_row("3", "Sair", "Encerrar conexão")

    console.print(table)


def jogar_fase(quant_caracteres):
    pool_caracteres, codigo_secreto = gerar_codigo_secreto(quant_caracteres)

    console.print(
        Panel(
            f"[bold bright_cyan]Caracteres interceptados:[/bold bright_cyan]\n\n"
            f"[bright_magenta]{'  '.join(pool_caracteres)}[/bright_magenta]\n\n"
            f"[white]Use apenas esses {quant_caracteres} caracteres.[/white]\n"
            f"[yellow]Descubra a ordem correta da senha.[/yellow]",
            title="[bold bright_cyan]DADOS CAPTURADOS[/bold bright_cyan]",
            border_style="bright_magenta"
        )
    )

    start_time = time.time()
    tentativas = 0

    while True:
        palpite = Prompt.ask(
            f"[bold green_yellow]root@cyberterminal[/bold green_yellow]"
            f":[bright_cyan]~[/bright_cyan]$ "
            f"Digite os {quant_caracteres} caracteres "
            f"([bright_red]0 para desistir[/bright_red])"
        ).strip().upper()

        if palpite == "0":
            console.print(
                Panel(
                    "[bold bright_red]MISSÃO ABORTADA[/bold bright_red]\n\n"
                    "[yellow]Retornando ao menu principal...[/yellow]",
                    border_style="bright_red"
                )
            )
            time.sleep(1.5)
            return

        if len(palpite) != quant_caracteres:
            console.print(
                f"[bold bright_red][ERRO][/bold bright_red] "
                f"O palpite deve ter exatamente {quant_caracteres} caracteres.\n"
            )
            continue

        if sorted(palpite) != sorted(pool_caracteres):
            console.print(
                "[bold bright_red][ERRO][/bold bright_red] "
                "Use apenas os caracteres mostrados.\n"
            )
            continue

        tentativas += 1

        posicoes_certas = sum(
            1 for a, b in zip(palpite, codigo_secreto) if a == b
        )

        if posicoes_certas == quant_caracteres:
            tempo_total = time.time() - start_time
            minutos = int(tempo_total // 60)
            segundos = int(tempo_total % 60)

            if minutos > 0:
                tempo_formatado = f"{minutos} minuto(s) e {segundos} segundo(s)"
            else:
                tempo_formatado = f"{segundos} segundos"

            console.print(
                Panel(
                    f"[bold bright_green]ACESSO TOTAL CONCEDIDO![/bold bright_green]\n\n"
                    f"[bright_cyan]Senha decifrada:[/bright_cyan] [white]{codigo_secreto}[/white]\n"
                    f"[bright_cyan]Tentativas:[/bright_cyan] {tentativas}\n"
                    f"[bright_cyan]Tempo total:[/bright_cyan] {tempo_formatado}\n\n"
                    f"[bold yellow]Sistema comprometido com sucesso.[/bold yellow]",
                    title="[bold bright_green]SENHA QUEBRADA[/bold bright_green]",
                    border_style="bright_green"
                )
            )
            break

        else:
            mensagem = (
                f"[bold bright_cyan]Resultado:[/bold bright_cyan] "
                f"{posicoes_certas} posição(ões) correta(s).\n\n"
                f"[yellow]Tentativa #{tentativas}[/yellow]\n"
            )

            if posicoes_certas == quant_caracteres - 1:
                mensagem += "\n[bright_magenta]Quase lá hacker... falta apenas uma posição.[/bright_magenta]"
            elif posicoes_certas >= 2:
                mensagem += "\n[bright_cyan]Boa tentativa. Continue o ataque.[/bright_cyan]"
            else:
                mensagem += "\n[bright_red]Acesso negado.[/bright_red]"

            console.print(
                Panel(
                    mensagem,
                    title="[bold bright_red]FALHA NA INVASÃO[/bold bright_red]",
                    border_style="bright_red"
                )
            )


tela_inicial()

while True:
    mostrar_menu()

    try:
        opcao = int(
            Prompt.ask("[bold green_yellow]Escolha o nível de invasão[/bold green_yellow]")
        )
    except ValueError:
        console.print("[bold bright_red]Digite apenas números válidos.[/bold bright_red]\n")
        continue

    if opcao == 1:
        jogar_novamente = "S"

        while jogar_novamente == "S":
            jogar_fase(3)
            jogar_novamente = Prompt.ask(
                "[bright_cyan]Deseja jogar novamente?[/bright_cyan] [S/N]"
            ).upper()

    elif opcao == 2:
        jogar_novamente = "S"

        while jogar_novamente == "S":
            jogar_fase(4)
            jogar_novamente = Prompt.ask(
                "[bright_cyan]Deseja jogar novamente?[/bright_cyan] [S/N]"
            ).upper()

    elif opcao == 3:
        console.print(
            Panel(
                "[bold bright_red]Conexão encerrada.[/bold bright_red]\n\n"
                "[yellow]Saindo do sistema...[/yellow]",
                border_style="bright_red"
            )
        )
        break

    else:
        console.print("[bold bright_red]Opção inválida.[/bold bright_red]\n")