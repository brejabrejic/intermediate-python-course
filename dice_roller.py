

def main():
  import random
  dice_sum = 0
  dice_Rolls = int(input("How many dice woukd you like to roll?"))
  dice_size = int(input("How many sides are the dice? "))
  for i in range(0,dice_size):
    roll = int(random.randint(1,6))
    dice_sum += roll
    if roll == 1:
      print("You rolled a ", roll, "!"," Critical Fail")
    elif roll == dice_size:
        print("You rolled a ", roll, " Critical success!")
    else:
      print("You rolled a ", roll)

  print("You have rolled a total of:", dice_sum)

if __name__== "__main__":
  main()