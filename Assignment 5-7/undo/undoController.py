class undoController:
    def __init__(self):
        self._operations = []
        self._index = -1    
        self._recorded = True

    def undo(self):
        if self._index < 0:
            return False
        
        self._recorded = False

        for oper in self._operations[self._index]:
            oper.undo()
    
        self._recorded = True
    
        self._index -= 1
        return True
    
    def redo(self):
        if self._index + 1 >= len(self._operations):
            return False
        
        self._recorded = False
        self._index += 1

        for item in self._operations[self._index]:
            item.redo()
    
        self._recorded = True
    
        return True

    def recordOperation(self, operation):
        if self._recorded == True:
            self._operations[-1].append(operation)

    def newOperation(self):
        if self._recorded == False:
            return

        self._operations = self._operations[0:self._index + 1]
        self._operations.append([])
        self._index += 1


class Operation:
    def __init__(self, functionUndo, functionDo):
        self._functionDo = functionDo
        self._functionUndo = functionUndo

    def undo(self):
        self._functionUndo.call()

    def redo(self):
        self._functionDo.call()

class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self._functionRef = functionRef
        self._parameters = parameters

    def call(self):
        self._functionRef(*self._parameters)

