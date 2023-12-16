from flet import *

class LoginView(UserControl):
  def __init__(self, page):
    super().__init__()

    self.view = View(
      "/login", 
      [
        AppBar(
          title=Text("Login"), 
          bgcolor=colors.SURFACE_VARIANT
        ),
        ElevatedButton(
          "Go Home", 
          on_click=lambda _: page.go("/")
        ),
      ],
    )