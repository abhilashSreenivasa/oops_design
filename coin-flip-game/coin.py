import random

class Coin:
    def __init__(self) -> None:
        self.coins=["head","tail"]
    def getRandomCoin(self):
        return self.coins[random.randint(0,1)]
