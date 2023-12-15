from flet import *
from utils.generic import Utils

class App():
    def __init__(self, page: Page):
        super().__init__()

        page.title = "Routes Class Example"

        def route_change(e):
            page.views.clear()
            page.views.append(
                Utils.switchRouter(page.route, page)
            )
            page.update()

        def view_pop(e):
            page.views.pop()
            top_view = page.views[-1]
            page.go(top_view.route)

        page.on_route_change = route_change
        page.on_view_pop = view_pop

        page.go(page.route)


app(target=App)