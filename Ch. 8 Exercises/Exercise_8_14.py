# Write a function storing the info of a car, must include manufacturer and 
# model, but also take in an arbitrary keyword parameter. Call the function and 
# print out the dictionary

def store_car(manufacturer, model, **car):
    """Stores info about a car into a dictionary and returns it"""
    car["manufactuer"] = manufacturer
    car["model"] = model

    return car

tlx = store_car("acura", "tlx",
                trim="aspec",
                year="2021",
                awd=True)

print(tlx)