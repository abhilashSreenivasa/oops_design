class Player:
    def __init__(self,name) :
        self.name=name
        self.coin=""
    def setCoin(self,coin):
        self.coin=coin
    def getCoin(self,coin):
        return self.coin
    