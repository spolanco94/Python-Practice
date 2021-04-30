locations = ["korea", "greece", "japan", "italy", "morocco"]

print(f"here is my list: {locations}")

print(f"\nThis is my list using 'sorted()': {sorted(locations)}")
print(f"This is my unchanged, original list: {locations}")

print(f"\nThis is my list in reverse using 'sorted()': {sorted(locations, reverse=True)}")
print(f"Again, here is my unchanged, original list: {locations}")

locations.reverse()
print(f"\nNow here is my list, changed using 'reverse()': {locations}")
locations.reverse()
print(f"Here is my original list restored by using 'reverse()': {locations}")

locations.sort()
print(f"\nHere is my list permanently changed by using 'sort()': {locations}")
locations.sort(reverse=True)
print(f"Here is my list in reverse alphabetical order using 'sort()': {locations}")