# Pet Class Example

# This program demonstrates the use of a Pet class to create instances of pets
# and display their attributes.

# Define the Pet class
class Pet:
    def __init__(self, name, species, age):
        # Initialize attributes
        self.__name = name
        self.__animal_type = species
        self.__age = age

    def set_name(self, name):
        # Set the name attribute
        self.__name = name
        return self.__name

    def set_animal_type(self, species):
        # Set the animal type attribute
        self.__animal_type = species
        return self.__animal_type

    def set_age(self, age):
        # Set the age attribute
        self.__age = age
        return self.__age

    def get_name(self, name):
        # Get the name attribute
        return self.__name

    def get_animal_type(self, species):
        # Get the animal type attribute
        return self.__animal_type

    def get_age(self, age):
        # Get the age attribute
        return self.__age

# Main function
def main():
    # Get user input for pet attributes
    name = input("Enter the name of your pet: ")
    species = input("Enter the type of your pet: ")
    age = input("Enter the age of your pet: ")

    # Create a Pet instance
    myPet = Pet(name, species, age)

    # Get the pet's attributes
    pet_name = myPet.get_name(name)
    pet_species = myPet.get_animal_type(species)
    pet_age = myPet.get_age(age)

    # Display pet information
    print("Hello " + pet_name + ". You are a " + pet_species + " that is " + pet_age + " years old.")

# Call the main function
if __name__ == "__main__":
    main()

