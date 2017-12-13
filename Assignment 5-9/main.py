from repository.PickleFileRepository import PickleFileRepository
from repository.repository import repository
from repository.BookCSVFileRepository import BookCSVFileRepository
from repository.ClientCSVFileRepository import ClientCSVFileRepository
from repository.RentalCSVFileRepository import RentalCSVFileRepository
from services.booksController import booksController
from services.clientsController import clientsController
from services.rentalController import rentalController
from ui.console import console
from undo.undoController import *

SETTINGS_FILE = "settings_text.properties"
#SETTINGS_FILE = "settings_binary.properties"

def readSettings():
    f = open(SETTINGS_FILE, "r")
    lines = f.read().split("\n")
    settings = {}
    
    for line in lines:
        setting = line.split("=")
        if len(setting) > 1:
            settings[setting[0]] = setting[1]
    f.close()
    return settings

settings = readSettings()

booksRepository = None
clientsRepository = None
rentalRepository = None

if 'Normal' == settings['repository']:
    booksRepository = repository()
    clientsRepository = repository()
    rentalRepository = repository()

if 'CSV' == settings['repository']:
    booksRepository = BookCSVFileRepository(settings['books'])
    clientsRepository = ClientCSVFileRepository(settings['clients'])
    rentalRepository = RentalCSVFileRepository(settings['rentals'])


if 'binary' == settings['repository']:
    booksRepository = PickleFileRepository(settings['books'])
    clientsRepository = PickleFileRepository(settings['clients'])
    rentalRepository = PickleFileRepository(settings['rentals'])

books_Controller = booksController(booksRepository)
clients_Controller = clientsController(clientsRepository)
rental_Controller = rentalController(booksRepository, clientsRepository, rentalRepository)
undo_Controller = undoController()

console = console(books_Controller, clients_Controller, rental_Controller, undo_Controller)
console.run()
