import random

def random_children():
  """Generates a random string with 3 G"s and "B"s, to show the girls and boys"""
  return "".join(random.choices(["G", "B"], k=3))

def simulate():
  """Runs  1000 times and returns the probability that,
if at least one of the children is a girl, all are girls."""
  all_girls = 0
  at_least_one_girl = 0
  for i in range(1000):
    children = random_children()
    if children == "GGG":
      all_girls += 1
    if "G" in children:
      at_least_one_girl += 1
  return all_girls / at_least_one_girl

print(simulate())
