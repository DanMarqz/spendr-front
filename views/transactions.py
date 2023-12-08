import flet as ft

transactionsView = ft.View(
                "/transactions",
                  [
                    ft.AppBar(
                      title=ft.Text("Transactions"), 
                      bgcolor=ft.colors.SURFACE_VARIANT
                    ),
                    ft.ElevatedButton(
                      "Go Home", 
                      on_click=lambda _: page.go("/")
                    ),
                  ],
                )