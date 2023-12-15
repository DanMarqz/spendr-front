from flet import *

class HomeView(UserControl):
  def __init__(self, page):
    super().__init__()

    self.view = View(
      "/",
      [
        AppBar(
          title=Text("Flet app"), 
          bgcolor=colors.SURFACE_VARIANT
        ),
        ElevatedButton(
          "Visit Store", 
          on_click=lambda _: page.go("/transactions")
        ),
        ElevatedButton(
          "Login", 
          on_click=lambda _: page.go("/login")
        ),
      ],
    )
  