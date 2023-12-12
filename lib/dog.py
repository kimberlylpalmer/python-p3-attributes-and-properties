#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
]


class Dog:
    def __init__(self, name="Fido", breed="Mastiff"):
        self.name = self.validate_name(name)
        self.breed = self.validate_breed(breed)

    def validate_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            return name
        else:
            print("Name must be string between 1 and 25 characters.")
            return "Invalid Name"

    def validate_breed(self, breed):
        if breed in APPROVED_BREEDS:
            return breed
        else:
            print("Breed must be in list of approved breeds.")
            return "Invalid Breed"
