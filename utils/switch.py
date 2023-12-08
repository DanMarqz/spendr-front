import flet as ft

from views.home import homeView
from views.transactions import transactionsView

def switchRouter(route='/', page=None):
  case = {
    '/': page.views.append(homeView),
    '/transactions': page.views.append(transactionsView)
  }
  return case.get(route, "Valor inválido")
