from repository.repo import repository
from size import getSize
from ui.console import console
from controler.controler import controler

size = getSize()
maxX = size[0]
maxY = size[1]
print (size)

gameRepository = repository(maxX, maxY)
gameControler = controler(gameRepository)
gameConsole = console(gameControler, maxX, maxY)
gameConsole.startGame()