# place = input("Choose a place: forest or cave? ")

# if place == "forest":
#     action = input("climb a tree or cross a river?")
#     if action =="climb a tree":
#         print("You found a bird's nest!")
#     elif place =="cave":
#         print("You find a hidden treasure!")
#     else:
#         print("You found a boat!")

#2
attendees = int(input("Enter number of attendees: "))
if attendees < 100:
    entertainment=input("audio systme or projector")
    if attendees<100 and entertainment=="audio system":
        print("Youll neeed the spaeker")
    elif attendees<100 and entertainment=="projector":
        print("Grab the projector")
else:
    print("Large hall")
food=input("Would you like some questionable vegeterian food: ")
if food=="yes":
    print("You will love Veggie Delight Caterers")
else:
    print("Gourmet Meals Caterers")


