motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

motorcycles.append("honda")
print(motorcycles)

motorcycles.insert(3, "toshiba")
print(motorcycles)

del motorcycles[3]
print(motorcycles)

last_owned = motorcycles.pop()
print(motorcycles)
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print(motorcycles)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

motorcycles = ['honda', 'yamaha', 'suzuki', "toshiba"]
print(motorcycles)
too_expensive = "toshiba"
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive + " is too expensive for me.")