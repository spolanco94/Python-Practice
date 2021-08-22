guests = ["Leonardo da Vinci", "Albert Einstein", "Elon Musk", "Eiichiro Oda"]

print(f"{guests[0]}, please join me for the brunch of the century!")
print(f"{guests[1]}, please join me for the brunch of the century!")
print(f"{guests[2]}, please join me for the brunch of the century!")
print(f"{guests[3]}, please join me for the brunch of the century!")

print(f"\nUnfortunately, {guests.pop(2)} has informed me that he cannot make it.")
guests.insert(2, "Bill Gates")
print(f"Instead, {guests[2]} will be coming in his place.")
print(f"As for {guests[0]}, {guests[1]}, and  {guests[3]}, I look forward to seeing the rest of you.")
