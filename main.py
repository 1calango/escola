import flet as ft


def main(page: ft.Page):
    page.title = "Teste do Flet"

    texto = ft.Text(
        "Flet funcionando!!!!",
        size=30
    )

    page.add(texto)


ft.run(main)