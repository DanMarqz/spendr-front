from views.home import HomeView
from views.transactions import TransactionsView
from views.login import LoginView

class Utils():
  def __init__(self, page):
    super().__init__()

    def switchRouter(route='/', page=None):
      case = {
        '/':              HomeView(page).view,
        '/transactions':  TransactionsView(page).view,
        '/login':         LoginView(page).view
      }
      return case.get(route, "Valor inválido")
