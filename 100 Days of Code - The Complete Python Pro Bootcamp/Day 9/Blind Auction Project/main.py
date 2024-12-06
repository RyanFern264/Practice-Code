# TODO-1: Ask the user for input
more_bidders = True
auction = {}
current_highest_bidder = ""
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    bidder_check = input("Are there any other bidders? Type 'yes' or 'no'")
    while not (bidder_check == "yes" or bidder_check == "no"):
        bidder_check = input("Can you stop being a dork and type it correctly")

    print("\n" * 20)
    current_highest_bidder = ""
    current_highest_bid = 0
    for name in auction:
        if auction[name] > current_highest_bid:
            current_highest_bidder = name
            current_highest_bid = auction[name]

    if bidder_check == "yes":
        more_bidders = True
    elif bidder_check == "no":
        more_bidders = False
print(f"The winner is {current_highest_bidder} with a bid of {auction[current_highest_bidder]}")


# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


