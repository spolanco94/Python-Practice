guests = ["Leonardo da Vinci", "Albert Einstein", "Elon Musk", "Eiichiro Oda"]

print(f"{guests[0]}, please join me for the brunch of the century!")
print(f"{guests[1]}, please join me for the brunch of the century!")
print(f"{guests[2]}, please join me for the brunch of the century!")
print(f"{guests[3]}, please join me for the brunch of the century!")

print(f"\nUnfortunately, {guests.pop(2)} has informed me that he cannot make it.")
guests.insert(2, "Bill Gates")

print(f"\nInstead, {guests[2]} will be coming in his place.")
print(f"As for {guests[0]}, {guests[1]}, and  {guests[3]}, I look forward to seeing the rest of you.")

print("\nGreat news! I have found a bigger table with room for more guests!")
guests.insert(0, "Christopher Nolan")
guests.insert(2, "Hideo Kojima")
guests.append("Paul Thomas Anderson")

print(f"\n{guests[0]}, please join me for the brunch of the century!")
print(f"{guests[1]}, please join me for the brunch of the century!")
print(f"{guests[2]}, please join me for the brunch of the century!")
print(f"{guests[3]}, please join me for the brunch of the century!")
print(f"{guests[4]}, please join me for the brunch of the century!")
print(f"{guests[5]}, please join me for the brunch of the century!")
print(f"{guests[6]}, please join me for the brunch of the century!")

print("\n\nApologies! Because of a last minute mix up, I can only invite two for brunch.")

print(f"\nSorry, {guests.pop()}, you did not make the cut. Maybe next time!")
print(f"Sorry, {guests.pop()}, you did not make the cut. Maybe next time!")
print(f"Sorry, {guests.pop()}, you did not make the cut. Maybe next time!")
print(f"Sorry, {guests.pop()}, you did not make the cut. Maybe next time!")
print(f"Sorry, {guests.pop(1)}, you did not make the cut. Maybe next time!")

print(f"\nAs for {guests[0]} and {guests[1]}, you are both still invited! I look forward to seeing you soon!")
del(guests[0])
del(guests[0])
print(guests)
