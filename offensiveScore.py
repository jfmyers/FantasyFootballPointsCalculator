from base import Base

class OffensiveScore(Base):
    def __init__(self, player):
        self.player = player

    def setOffensivePenalties(self):
        player = self.player
        #penalties
        penalties = (int(player.passing_ints) + int(player.fumbles_lost)) * -2
        self.offensivePenaltiesScore = penalties
    
    def getTotalScore(self):
        self.setTD()
        self.set2Pt()
        self.setPassingYds()
        self.setRushingYds()
        self.setOffensivePenalties()
        
        self.totalScore = self.tdScore + self.twoPtScore + self.passingScore + self.rushingScore + self.offensivePenaltiesScore
        return self.totalScore