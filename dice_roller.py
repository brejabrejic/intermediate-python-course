

def main():
  import random
  dice_sum = 0
  dice_Rolls = 2
  for i in range(0,dice_Rolls):
    roll = int(random.randint(1,6))
    dice_sum += roll
    print('You rolled a', roll)
  print("You have rolled a total of:", dice_sum)

if __name__== "__main__":
  main()