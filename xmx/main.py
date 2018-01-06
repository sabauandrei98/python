from repository.repo import repository
from ui.console import console
from controler.controler import controler

gameRepository = repository()
gameControler = controler(gameRepository)
gameConsole = console(gameControler)
gameConsole.startGame()