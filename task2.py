class Dog:
    # Class attribute age_factor set to 7
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        # Calculate the human age equivalent
        return self.dog_age * Dog.age_factor



dog_instance = Dog(5)


human_equivalent_age = dog_instance.human_age()
print(human_equivalent_age)
