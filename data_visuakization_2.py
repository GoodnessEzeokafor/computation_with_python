def findPayment(loan, r, m):
    """
    Assumes: loan and r are floats, m an int
    Returns the monthly payment for a mortage of sie loan at a monthly
    rate of r for m months
    """
    return loan*((r*(1+r)**m) / ((1+r)**m - 1))


class Mortage(MortagePlots, object):
    """
    Abstract class for building differen kinds of mortages
    """
    def __init__(self, loan, annRate, months):
        self.loan = loan
        self.rate = ammRate/12
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend =None # description of moratage
    

    def makePayment(self):
        """ Make A Payment"""   
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    
    def getTotalPaid(self):
        """ Return the total amount paid so far"""
        return sum(self.paid)
    
    def __str__(self):
        return self.legend


class Fixed(Mortage):
    def __init__(self, loan, r, months):
        Mortage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + "%"

class FixedWithPts(Mortage):
    def __init__(self, loan, r, months):
        Mortage.__init__(self, loan, r, months)
        self.pts = ptsself.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + "%" + str(pts) + ' points'

class TwoRate(Mortage):
    def __init__(self, loan, r, months, teaserRate, teaserMonths):
        Mortage.__init__(self, loan, teaserRate, months)
        self.teaserMonths = teaserMonths
        self.teaserRate = teaserRate
        self.nextRate = r/12.0
        self.legend = str(teaserRate*100) + '% for ' + str(self.teaserMonths) + ' months,\n' + str(r*100) + '%'


    def makePayment(self):
        if len()self.paid  == self.teaserMonths + 1:
            self.rate = self.nextRateself.payment = findPayment(
                                                    self.owed[-1],
                                                    self.rate,
                                                    self.months - self.teaserMonths
                                                    )
        Mortage.makePayment(self)
        