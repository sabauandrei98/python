from raiseEx import raiseException


class validate:

    #CHECKS IF DNA CONTAINS ONLY 'ACTG'
    @staticmethod
    def validateDNA(s):
        for x in s.getDna():
            if x not in "ACTG":
                raise raiseException("DNA not ok")
        return True


    @staticmethod
    def validateLen(s):
        if len(s.getDna()) > 100:
            raise raiseException("DNA too long")
        return True