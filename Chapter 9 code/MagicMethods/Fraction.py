class Fraction():
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def getValue(self):
        return self.value

    def __str__(self):
        '''Create a string representation of the fraction'''
        output = 'Fraction: ' + str(self.numerator) + '/' + \
                 str(self.denominator) + '\n' +\
                'Value: ' + str(self.value) + '\n'
        return output

    def _leastCommonMultiple(self, value1, value2):
        '''Calculate the least common multiple of the two denominators'''
        if(value1 > value2):
            theLCM = value1
        else:
            theLCM = value2
        while True:
            if (theLCM % value1) == 0 and (theLCM % value2) == 0:
                return theLCM
            theLCM = theLCM + 1       

    def __add__(self, oOtherFraction):
        ''' Add two Fraction objects'''
        newDenominator = self._leastCommonMultiple(self.denominator, oOtherFraction.denominator)
        
        selfMultiplicationFactor = newDenominator / self.denominator
        selfEquivalentNumerator = self.numerator * selfMultiplicationFactor
     
        otherMultiplicationFactor = newDenominator / oOtherFraction.denominator
        oOtherFractionEquivalentNumerator = oOtherFraction.numerator * otherMultiplicationFactor

        newNumerator = int(selfEquivalentNumerator + oOtherFractionEquivalentNumerator)

        oAddedFraction = Fraction(newNumerator, newDenominator)
        return oAddedFraction

    def __eq__(self, oOtherFraction):
        '''Test for equality '''
        return (self.value == oOtherFraction.value)
        

oFraction1 = Fraction(1, 3)  # create a Fraction object
print(oFraction1)  # print the object ... calls  __str__

oFraction2 = Fraction(2, 5)
print(oFraction2)

oSumFraction = oFraction1 + oFraction2  # calls __add__
print(oSumFraction)

print(oFraction1 == oFraction2)  # should be False
