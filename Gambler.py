"""
   * author - Akshay Tekam
   * date - 12/01/2021
   * time - 09:12:23
   * package - ${PACKAGE_NAME}
   * Title - Simulates a gambler who start with $stake
   and place fair $1 bets until he/she goes broke
   (i.e. has no money) or reach $goal.
"""
import random
class Gambler:
    def __init__(self, bets=1, stake=2, goals=6, count=0, win=0):
        self.bets=bets
        self.goals=goals
        self.money=stake
        self.count=count
        self.win=win
    # gambling with total stake until you go broke or reach goal
    def gambling(self):
        while self.money!=0 or self.money==self.goals:
            toss=random.randrange(0, 2)            # Random function to get value between 0 and 1
            if toss < 0.5:
                self.money -=1
            elif toss > 0.5:
                self.money +=1
                self.win +=1
            self.count +=1                        # count the total bets
        return self.count
    # Displaying the percent of win or loss
    def percentOfWinLoss(self):
        percentOfWin = (self.win * 100) / self.count
        percentOfLoss = ((self.count - self.win) * 100) / self.count

        print("Total wins:" + str(self.win))
        print("Percent of wins:" + str(percentOfWin))
        print("Percent of loss:" + str(percentOfLoss))
obj=Gambler()
obj.gambling()                     # creating object and calling function
obj.percentOfWinLoss()




