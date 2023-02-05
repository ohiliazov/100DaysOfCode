import replit

logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}
should_continue = "yes"

while should_continue.lower() == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))

    bidders[name] = bid

    should_continue = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n"
    )

    replit.clear()

sorted_bidders = sorted(bidders.items(), key=lambda item: item[1], reverse=True)

winner_name, winner_bid = sorted_bidders[0]
print(f"The winner is {winner_name} with a bid of ${winner_bid:.2f}")
