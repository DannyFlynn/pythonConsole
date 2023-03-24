from money import Money
from game import Game

def main():
  user = Money()
  money_inserted = user.insert_money()
  user = Game(money_inserted)


  gameover = False

  while gameover == False:
    print(f"Funds: £{user.money}")
    if user.money == 0:
      print("You are out of funds")
      main()
      break

    choice = input("Spin (s) or Cash out (c): ")
    if choice == 's':
        user.money -= 1
        player_spin = user.spin()
        user.win_or_loss(player_spin)

    elif choice == 'c':
        gameover = True
        change_given = user.cashout()
        print(f"Change Given: £{change_given}")
        print("Thank you for using our machine please come again")
        main()



main()
