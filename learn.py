def edit_pets():
    pets = ["Luna","Cody","Ally","Lincoln"]
    pets.pop(1)
    pets.append("Bella")
    pets += ["Buddy"]
    return pets
dogs = edit_pets()
print(dogs)
