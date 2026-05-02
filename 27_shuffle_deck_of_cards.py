import random 
ranks = '23456789tjqka'
suits ='♠♥♦♣'
deck = [r + s for r in ranks for s in suits]
random.shuffle(deck)
print(deck[:5]) # Print the first 5 cards from the shuffled deck