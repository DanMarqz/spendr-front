import flet as ft

def main(page: ft.Page):
    header = ft.Text(
        value="Spendr!", 
        color="green",
        style=ft.TextThemeStyle.DISPLAY_LARGE
    )
    description = ft.Text(
        value="An assistant to help you with home planification!",
        color="#03DAC5",
        italic=True,
        style=ft.TextThemeStyle.DISPLAY_SMALL
    )
    comingSoon = ft.ElevatedButton("Working in something amazing")
    pb = ft.ProgressBar(width=400)
    page.add(
        #ft.Text("Linear progress indicator", style="headlineSmall"),
        header,
        ft.Column([ description, pb]),
        comingSoon
    )
    # page.controls.append(header)
    # page.controls.append(description)
    page.update()

ft.app(port=8080, target=main, view=ft.AppView.WEB_BROWSER)