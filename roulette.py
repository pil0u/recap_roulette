from random import choice
from time import sleep

STUDENTS = [
  'Name 1',
  'Name 2',
  'Name 3',
]

def rien_ne_va_plus(hot_seats, safe_students):
    
  if hot_seats == []:
    hot_seats = STUDENTS.copy()
    safe_students = []

  print(f"Students on the hot seats for the next question:\n\t{', '.join(hot_seats)}\n")
  sleep(1)
  print(f"Safe students (for now):\n\t{'Nobody 😈' if safe_students == [] else ', '.join(safe_students)}\n")
  sleep(1)

  the_chosen_one = choice(hot_seats)
  hot_seats.remove(the_chosen_one)
  safe_students.append(the_chosen_one)

  print("The chosen one is", end=" ")
  for i in range(3):
      print('.', end="")
      sleep(1)
  print(f" {choice(['🎉', '🥳', '🎊'])} {the_chosen_one.upper()} {choice(['🎉', '🥳', '🎊'])}")

  return hot_seats, safe_students
