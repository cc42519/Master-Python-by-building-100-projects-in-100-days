# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

blind_auction = {}
more_input = "y"

while more_input == "y":
    print("\n" * 20)
    name = input("input name:")
    price = int(input("input price:"))
    blind_auction[name] = price
    more_input = input("more input (y/n):")
max_bid = 0
bid = 0
for person in blind_auction:
    bid = blind_auction[person]
    if bid > max_bid:
        max_bidder = person
print(blind_auction)
print(f"The winner of the blind auction is {max_bidder}")