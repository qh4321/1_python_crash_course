players = ['charles', 'emma', 'mechael', 'trump', 'eli']
print(players[0:3])
print(players[2:])
print(players[:3])
print(players[-3:])

print("\nHere are the first three players on my team:")
for player in players[0:3]:
    print(player.title())