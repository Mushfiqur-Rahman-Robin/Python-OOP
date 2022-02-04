import random
from unittest import result
value = random.random()
print(value)

value = random.uniform(1, 10)
print(value)

value = random.randint(1, 15)
print(value)

greetings = ['Hi', 'Hello', 'Hola', 'Hey']

value = random.choice(greetings)
print(value + ' user!')

colors = ['Red', 'Green', 'Black']

results = random.choices(colors, weights=[18, 2, 18], k=10)
print(results)  # ['Red', 'Green', 'Black', 'Green', 'Red', 'Green', 'Red', 'Red', 'Black', 'Green']  



deck = list(range(1,53))
random.shuffle(deck)
print(deck) 

hand = random.sample(deck, k=5)
print(hand)