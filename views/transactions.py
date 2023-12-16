from flet import *

class TransactionsView(UserControl):
  def __init__(self, page):
    super().__init__()

    self.view = View(
      "/transactions", 
      [
        AppBar(
          title=Text("Transactions"), 
          bgcolor=colors.SURFACE_VARIANT
        ),
        ElevatedButton(
          "Go Home", 
          on_click=lambda _: page.go("/")
        ),
      ],
    )