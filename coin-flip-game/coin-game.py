
from coin import Coin
from player import Player
import random
class CoinGame:
    def __init__(self,p1,p2):
        self.players=[Player(p1),Player(p2)]
        self.choices=["head","tail"]
        self.opposite={"head":"tail",
                       "tail":"head"}

    def choose(self):
        return self.choices[random.randint(0,1)]
    
    def toss(self):
        return Coin().getRandomCoin()
    
    def playGame(self):
        gameContinue=True
        while gameContinue:
            player_id=random.randint(0,1)
            choice=self.choose()
            print(self.players[player_id].name," got to choose and he chose ",choice)

            self.players[player_id].setCoin(choice)
            if player_id==1:
                self.players[0].setCoin(self.opposite[choice])
            else:
                self.players[1].setCoin(self.opposite[choice])
            
            res=self.toss()
            print("Coin is in the air and we got a ", res, "!")
            if res==choice:
                print(self.players[player_id].name," wins the game!")
            else:
                other_player=0
                if player_id==0:
                    other_player=1
                print(self.players[other_player].name, "wins the game!")

            inp=input("Wanna play one more? Type y, n otherwise:")
            if inp=="y":
                gameContinue=True
            else:
                gameContinue=False

CoinGame("Abhi","Sandesh").playGame()

            







