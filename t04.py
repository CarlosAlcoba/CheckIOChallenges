cake_pieces = int(input("Number of pieces of cake: "))
guests = int(input("Number of party-goers: "))
cake_per_guest = cake_pieces // guests
extra_cake = cake_pieces % guests

print()
print(f"Each party-goer receives {cake_per_guest} pieces of cake")
print(f"Pieces of cake that won’t be distributed: {extra_cake}")