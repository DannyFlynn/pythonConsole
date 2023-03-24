from data import slots
import random

class Game:

  def __init__(self, money):
      self.prizeboard = [
          {"symbol": "XXX", "payout": 5},
          {"symbol": "OOO", "payout": 10},
          {"symbol": "PPP", "payout": 40},
          {"symbol": "JJJ", "payout": 100},
      ]
      self.money = money


  def spin(self):
        player_spin = random.sample(slots, 3)
        print(player_spin)
        return player_spin


  def win_or_loss(self, spin_results):

      spin_results = ''.join(spin_results)
      for reel in self.prizeboard:

          if spin_results in reel['symbol']:

             print(reel['symbol'])
             self.money += reel['payout']
             print(f"Congratulations you just won £{reel['payout']}")


  def cashout(self):
      return self.money





