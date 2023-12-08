import flet as ft

homeView = ft.View(
            "/",
              [
                ft.AppBar(
                  title=ft.Text("Flet app"), 
                  bgcolor=ft.colors.SURFACE_VARIANT
                ),
                ft.ElevatedButton(
                  "Visit Store", 
                  on_click=lambda _: page.go("/transactions")
                ),
              ],
          )