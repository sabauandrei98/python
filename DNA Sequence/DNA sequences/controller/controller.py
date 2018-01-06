from domain.domain import DNA
from validate import validate

class controller:

    def __init__(self, repository):
        self.__repository = repository

    # ADD DNA TO THE LIST
    def addDna(self, param):
        dna = DNA(param)
        validate.validateDNA(dna)
        validate.validateLen(dna)
        self.__repository.addItem(dna)

    # FILTER DNA BY SEQUENCE, SORTED BY THE DNA LENGTH
    def filterDna(self, param):
        dna = DNA(param)
        validate.validateDNA(dna)
        validate.validateLen(dna)
        l = self.__repository.filter(dna)

        return sorted(l, key = lambda x: -len(x.getDna()))

    # PRINT DNA BY LONGEST REPEATING SAME LETTER SEQUENCE
    def sortLongestRepe(self):
        return sorted(self.__repository.getItems(), key = lambda x: -x.getLongestRep())

    #SIMPLE PRINT
    def show(self):
        for x in self.__repository.getItems():
            print (x)
