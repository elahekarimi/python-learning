import os

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


bridding_finish= False
bids={}
def find_highest_bidder(bidding_record):
    highest_bid=0
    winer=""
    for bidder in bidding_record:
        bid_amout=bidding_record[bidder]
        if bid_amout > highest_bid:
            highest_bid = bid_amout
            winer=bidder
    print(f"the winer is {winer} with a bid of{highest_bid}")


while not bridding_finish:
    name=input("what is your name:")
    price=int(input("what is your price: $"))
    bids[name]=price
    should_continue=input("Are there any bridders? say yes or no\n")
    if should_continue == "no": 
        bridding_finish = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clearConsole()
