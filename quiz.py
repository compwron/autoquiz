from random import randint
from random import sample
from datetime import datetime

MAX = 12
symbols = ['+', '-', '*', '*']
should_continue = True

wins = 0
tries = 0
start_time = datetime.now()

while should_continue:
  tries += 1
  equation = str(randint(0, MAX)) + " " + sample(symbols, 1)[0] + " " + str(randint(0,MAX)) + "\n"
  answer = eval(equation)
  user_says = input(equation)
  if "done" in user_says:
    should_continue = False
    tries -= 1
  elif int(user_says) == answer:
    print("Correct!")
    wins += 1
  else:
    print("Wrong. Answer is: " + str(answer))

end_time = datetime.now()
total_time = (end_time - start_time).total_seconds()
print(str(wins) + " wins / " + str(tries) + " tries in " + str(round(total_time, 2)) + " sec (" + str(round(total_time / tries, 2)) + " sec per try)")
