from ui.console import console
from repo.repository import repository
from controller.controller import controller


'''
WIRE UP ALL THE CLASSES
'''
dnaRepo = repository()
dnaController = controller(dnaRepo)
dnaConsole = console(dnaController)
dnaConsole.run()

