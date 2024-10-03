# Secret Auction Programme
print("Welcome! to Secret Auction\n\n")
auction={}
person=True
while(person==True):
    a = input("Enter your name :\n")
    b = int(input("Enter your bid in RS. :\n"))
    auction[a]=b
    c=input("Any other wants to Bid ?(y-yes,n-no)\n").lower()
    if c=="y":
        person=True
        print("\n"*100)
    else:
        person=False
        print("\n"*100)
max_price= max(auction,key=auction.get)
max_auction_price=auction[max_price]
print(f"The maximum value bidder is {max_price} and the bid is of RS. {max_auction_price}")
