import flet as ft

def main(page: ft.Page):
    page.title = "Routes Example"

    def route_change(e):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                    [
                        ft.AppBar(
                            title=ft.Text("Budget Admin"), 
                            bgcolor=ft.colors.SURFACE_VARIANT
                        ),
                        ft.ElevatedButton(
                            "Transactions", 
                            on_click=lambda _: page.go("/transactions")
                        ),
                    ],
            )
        )
        if page.route == "/transactions":
            page.views.append(
                ft.View(
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
            )
        page.update()

    def view_pop(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go(page.route)


ft.app(main)