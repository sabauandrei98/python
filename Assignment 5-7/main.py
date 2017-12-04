from repository.repository import repository
from services.booksController import booksController
from services.clientsController import clientsController
from services.rentalController import rentalController
from ui.console import console
from undo.undoController import *

booksRepository = repository()
clientsRepository = repository()
rentalRepository = repository()

books_Controller = booksController(booksRepository)
clients_Controller = clientsController(clientsRepository)
rental_Controller = rentalController(booksRepository, clientsRepository, rentalRepository)
undo_Controller = undoController()

console = console(books_Controller, clients_Controller, rental_Controller, undo_Controller)
console.run()
