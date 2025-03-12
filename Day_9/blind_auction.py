from blind_auction_art import logo
print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


print("Hello, Welcome to the Blind Auction")
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"This is the end of the auction.The winning bid was {winner} with a ${highest_bid} bid.")

bidders = {}
more_bidders = True
while more_bidders:
    names = input("What is your name? ")
    bids = int(input("What is your bid?"))

    bidders[names] = bids

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if more_bidders == 'no':
        more_bidders = False
        find_highest_bidder(bidders)
    elif more_bidders == 'yes':
        print("\n" * 20)

