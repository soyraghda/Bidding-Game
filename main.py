from replit import clear
end_bid=False
bidding={}

def find_winner(bids):
    max=0
    winner=""
    for bidder in bids:
      if bids[bidder] > max:
         max=bids[bidder]
         winner=bidder
    print(f"The highest bidder is {winner} with the amount of ${max}")

while(end_bid != True):
   name=input("please enter your name:")
   bid=int(input("please enter your bid:"))
   bidding[name]=bid
   end=input("Are there any other bidders? Type 'yes or 'no'.\n")
   clear()
    
   if(end.lower()=="no"):
    end_bid=True
       
find_winner(bidding)


