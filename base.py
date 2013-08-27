class Base:
    def __init__(self, player):
        self.player = player
        
    #Methods for calculating mainly offensive scores
    
    def setTD(self):
        player = self.player
        #td score
        score = ((int(player.rushing_tds) + int(player.receiving_tds) + int(player.kickret_tds) + int(player.puntret_tds)) * 6) + (int(player.passing_td) * 4)
        self.tdScore = score;
    
    def set2Pt(self):
        player = self.player
        #twoPt
        score = (int(player.rushing_twoptm) + int(player.receiving_twoptm) + int(player.passing_twoptm)) * 2
        self.twoPtScore = score
    
    def setPassingYds(self):
        player = self.player
        #passing yds
        score = int(player.passing_yds) / 25
        self.passingScore = score
    
    def setRushingYds(self):
        player = self.player
        #rushing yds
        score = (int(player.rushing_yds) + int(player.receiving_yds)) / 10
        self.rushingScore = score    
    
    #Methods for calculating mainly kicker scores
    
    #Method for calculating defensive/special teams scores
    