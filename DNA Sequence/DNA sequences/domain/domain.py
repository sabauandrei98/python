class DNA:
    def __init__(self, dna):
        self.__dna = dna

    #SET DNA
    def setDna(self, newDna):
        self.__dna = newDna
    #GET DNA
    def getDna(self):
        return self.__dna

    #GETS THE NUMBER OF CONTINUOUS LETTERS IN DNA
    def getLongestRep(self):
        bst = 0
        k = 1
        for x in range(0, len(self.__dna) - 1):
            if self.__dna[x] == self.__dna[x+1]:
                k += 1
                bst = max(k, bst)
            else:
                k = 1

        return bst

    #TO STRING
    def __str__(self):
        return self.__dna
    #GET LENGTH
    def __len__(self):
        return len(self.__dna)
