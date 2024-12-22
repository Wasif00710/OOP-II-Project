from typing import Dict, List, Any
from datetime import date


'''
    We tried to impliment a lot of operations but when we tried to impliment we faced many problems
    and so we tried to keep it simple but still we created all the classes and subclasses for our 
    intended project.
'''


#================================================================================================
#================================================================================================
#===========================                          ===========================================
#===========================         Taufik           ===========================================
#===========================                          ===========================================
#================================================================================================
#================================================================================================

# Base class representing a pet
class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age
        self.health_data = {}  # Dictionary to store health-related data

    # Method to update a specific health data attribute
    def update_health_data(self, key: str, value: Any):
        self.health_data[key] = value

    # Method to retrieve all health data for the pet
    def get_health_data(self) -> Dict[str, Any]:
        return self.health_data

    # Method to get general details about the pet
    def get_details(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "health_data": self.health_data
        }

# Subclass for dog care
class DogCare(Pet):
    # Dog-specific schedule
    def get_schedule(self) -> str:
        return "Daily walk: 7 AM, Feed: 8 AM and 6 PM"

# Subclass for cat care
class CatCare(Pet):
    # Cat-specific schedule
    def get_schedule(self) -> str:
        return "Feed: 8 AM and 7 PM, Litter box check: 9 PM"

# Subclass for bird care
class BirdCare(Pet):
    def __init__(self, name: str, species: str, age: int, wing_span: float):
        super().__init__(name, species, age)
        self.wing_span = wing_span  # Additional attribute specific to birds

    # Bird-specific schedule
    def get_schedule(self) -> str:
        return "Feed: 9 AM and 5 PM, Cage cleaning: 10 AM"

    # Include wing span in details
    def get_details(self) -> Dict[str, Any]:
        details = super().get_details()
        details["wing_span"] = self.wing_span
        return details

# Subclass for rabbit care
class RabbitCare(Pet):
    def __init__(self, name: str, species: str, age: int, favorite_food: str):
        super().__init__(name, species, age)
        self.favorite_food = favorite_food  # Additional attribute specific to rabbits

    # Rabbit-specific schedule
    def get_schedule(self) -> str:
        return "Feed: 8 AM and 7 PM, Playtime: 4 PM"

    # Include favorite food in details
    def get_details(self) -> Dict[str, Any]:
        details = super().get_details()
        details["favorite_food"] = self.favorite_food
        return details

# Class representing an appointment for a pet
class Appointment:
    def __init__(self, appointment_id: str, pet_id: str, date: date):
        self.appointment_id = appointment_id
        self.pet_id = pet_id
        self.date = date

    # Retrieve appointment details
    def get_details(self) -> Dict[str, Any]:
        return {
            "appointment_id": self.appointment_id,
            "pet_id": self.pet_id,
            "date": self.date
        }

# Class representing a task for a pet
class Task:
    def __init__(self, task_id: str, pet_id: str, scheduled_time: date):
        self.task_id = task_id
        self.pet_id = pet_id
        self.scheduled_time = scheduled_time
        self.done = False  # Status of the task

    # Mark the task as completed
    def mark_as_done(self):
        self.done = True

# Class for managing health records
class HealthRecord:
    def __init__(self, record_id: str, pet_id: str, condition: str):
        self.record_id = record_id
        self.pet_id = pet_id
        self.condition = condition

    # Retrieve health record details
    def get_health_details(self) -> Dict[str, Any]:
        return {
            "record_id": self.record_id,
            "pet_id": self.pet_id,
            "condition": self.condition
        }

# Class for managing pet tasks
class TaskManager:
    def __init__(self):
        self.tasks = {}  # Dictionary to store tasks for each pet

    # Add a new task for a specific pet
    def add_task(self, pet_name: str, task_type: str, due_date: str):
        if pet_name not in self.tasks:
            self.tasks[pet_name] = []
        self.tasks[pet_name].append({"task_type": task_type, "due_date": due_date, "done": False})

    # Get all tasks for a specific pet
    def get_tasks(self, pet_name: str) -> List[Dict[str, Any]]:
        return self.tasks.get(pet_name, [])

    # Mark a specific task as done
    def mark_task_done(self, pet_name: str, task_type: str):
        for task in self.tasks.get(pet_name, []):
            if task["task_type"] == task_type:
                task["done"] = True

# Class for managing vaccinations
class Vaccination:
    def __init__(self):
        self.records = {}  # Dictionary to store vaccination records

    # Add a new vaccination record
    def add_vaccination(self, pet_name: str, vaccine_name: str, due_date: str):
        if pet_name not in self.records:
            self.records[pet_name] = []
        self.records[pet_name].append({"vaccine_name": vaccine_name, "due_date": due_date})

    # Get vaccination records for a pet
    def get_vaccinations(self, pet_name: str) -> List[Dict[str, Any]]:
        return self.records.get(pet_name, [])

# Class for managing feeding schedules
class FoodManager:
    def __init__(self):
        self.feeding_schedules = {}  # Dictionary to store feeding times

    # Add a feeding time for a specific pet
    def add_feeding_time(self, pet_name: str, time: str):
        if pet_name not in self.feeding_schedules:
            self.feeding_schedules[pet_name] = []
        self.feeding_schedules[pet_name].append(time)

    # Get feeding schedule for a pet
    def get_feeding_schedule(self, pet_name: str) -> List[str]:
        return self.feeding_schedules.get(pet_name, [])

# Class for managing boarding records
class Boarding:
    def __init__(self):
        self.boarding_records = {}  # Dictionary to store boarding records

    # Add a boarding record for a pet
    def add_boarding(self, pet_name: str, start_date: str, end_date: str, location: str):
        if pet_name not in self.boarding_records:
            self.boarding_records[pet_name] = []
        self.boarding_records[pet_name].append({"start_date": start_date, "end_date": end_date, "location": location})

    # Get boarding records for a pet
    def get_boarding_records(self, pet_name: str) -> List[Dict[str, Any]]:
        return self.boarding_records.get(pet_name, [])

# Class for managing adoption records
class Adoption:
    def __init__(self):
        self.adoption_records = {}  # Dictionary to store adoption status

    # Update adoption status for a pet
    def update_adoption_status(self, pet_name: str, status: str):
        self.adoption_records[pet_name] = status

    # Get adoption status for a pet
    def get_adoption_status(self, pet_name: str) -> str:
        return self.adoption_records.get(pet_name, "Not adopted")

# Main class for organizing pet care activities
class PetCareOrganizer:
    def __init__(self):
        self.pets = {}  # Dictionary to store all pets
        self.task_manager = TaskManager()
        self.vaccination = Vaccination()
        self.food_manager = FoodManager()
        self.boarding = Boarding()
        self.adoption = Adoption()

    # Add a new pet to the organizer
    def add_pet(self, name: str, species: str, age: int, **kwargs):
        if species.lower() == "dog":
            self.pets[name] = DogCare(name, species, age)
        
        elif species.lower() == "cat":
            self.pets[name] = CatCare(name, species, age)
        
        elif species.lower() == "bird":
            wing_span = kwargs.get("wing_span", 0.0)
            self.pets[name] = BirdCare(name, species, age, wing_span)
        
        elif species.lower() == "rabbit":
            favorite_food = kwargs.get("favorite_food", "Unknown")
            self.pets[name] = RabbitCare(name, species, age, favorite_food)

    # Get details of a specific pet
    def get_pet_details(self, name: str) -> Dict[str, Any]:
        pet = self.pets.get(name)
        if pet:
            return pet.get_details()
        return {}

    # Display the schedule of a specific pet
    def display_schedule(self, name: str) -> str:
        pet = self.pets.get(name)
        if pet:
            return pet.get_schedule()
        return "No schedule available."






#================================================================================================
#================================================================================================
#===========================                                =====================================
#===========================   Details and Authentication   =====================================
#===========================                                =====================================
#================================================================================================
#================================================================================================


# A dictionary to store user data (mock database)
users = {
    "admin": {"password": "luluboss", "role": "admin", "balance": 0},
    "user": {"password": "lulu", "role": "user", "balance": 500}
}

# Sample product data for the shop
products = [
    {"id": 1, "name": "Dog Food", "price": 20},
    {"id": 2, "name": "Cat Toy", "price": 10},
    {"id": 3, "name": "Bird Cage", "price": 50},
    {"id": 4, "name": "Rabbit Bedding", "price": 15}
]

# Global instance of PetCareOrganizer
pet_care_organizer = PetCareOrganizer()

# Function to authenticate users
def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users and users[username]["password"] == password:
        return username
    
    else:
        print("Invalid username or password.")
        return None


#================================================================================================
#================================================================================================
#===========================                          ===========================================
#===========================         Maruf            ===========================================
#===========================                          ===========================================
#================================================================================================
#================================================================================================



# User menu functionality
def user_menu(username):
    """
    Function to display and manage the user menu.
    Allows users to view products, buy products, check balance, 
    view pet details, and now add pets.
    """
    while True:
        # Display user menu options
        print("\n--- User Menu ---")
        print("1. View Products")
        print("2. Buy Product")
        print("3. View Balance")
        print("4. View Pet Details")
        print("5. Add Pet")
        print("6. Logout")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            # Display available products
            print("\nAvailable Products:")
            for product in products:
                print(f"{product['id']}: {product['name']} - ${product['price']}")
            input("Enter any key to continue...")  # Pause to let the user review
        
        elif choice == "2":
            # Buying product flow
            while True:
                print("\nAvailable Products:")
                for product in products:
                    print(f"{product['id']}: {product['name']} - ${product['price']}")
                product_id = input("Enter product ID to buy (or 'b' to go back): ")

                if product_id.lower() == 'b':
                    break  # Return to main menu
                product = next((p for p in products if str(p["id"]) == product_id), None)

                print("\nEnter Payment method (or 'b' to go back): \n1. Cash Payment\n2. Online Payment")
                product_id = input("Enter your choice: ")

                if product_id.lower() == 'b':
                    break  # Return to main menu

                if product:
                    try:
                        # Check if the user has enough balance
                        if users[username]["balance"] >= product["price"]:
                            users[username]["balance"] -= product["price"]
                            users["admin"]["balance"] += product["price"]
                            print(f"You bought {product['name']} for ${product['price']}.")
                        else:
                            raise ValueError("Insufficient balance.")
                    except ValueError as e:
                        print(e)
                else:
                    try:
                        raise ValueError("Invalid product ID.")
                    except ValueError as e:
                        print(e)

                input("Enter any key to continue...")  # Pause after purchase
        
        elif choice == "3":
            # View user's current balance
            print(f"Your balance: ${users[username]['balance']}")
            input("Enter any key to continue...")  # Pause to let the user review
        
        elif choice == "4":
            # View pet details
            pet_name = input("Enter pet name: ")
            details = pet_care_organizer.get_pet_details(pet_name)

            if details:
                print("Pet Details:")
                for key, value in details.items():
                    print(f"{key.capitalize()}: {value}")
            
            else:
                print("Pet not found.")
            input("Enter any key to continue...")  # Pause to let the user review
        
        elif choice == "5":
            # Add a new pet
            name = input("Enter pet name: ")
            species = input("Enter pet species (Dog/Cat/Bird/Rabbit): ")
            age = int(input("Enter pet age: "))
            additional_data = {}

            # Collect species-specific data
            if species.lower() == "bird":
                additional_data["wing_span"] = float(input("Enter wing span: "))
            
            elif species.lower() == "rabbit":
                additional_data["favorite_food"] = input("Enter favorite food: ")
            pet_care_organizer.add_pet(name, species, age, **additional_data)
            print(f"Pet '{name}' added successfully.")
            input("Enter any key to continue...")  # Pause after adding pet
        
        elif choice == "6":
            # Exit the user menu
            break
        
        else:
            # Handle invalid input
            print("Invalid choice. Please try again.")








#================================================================================================
#================================================================================================
#===========================                          ===========================================
#===========================         Wasif            ===========================================
#===========================                          ===========================================
#================================================================================================
#================================================================================================



# Admin menu functionality
def admin_menu():
    """
    Function to display and manage the admin menu.
    Allows admin to add products, add pets, view pet details,
    update user balances, and exit the admin menu.
    """
    while True:
        # Display admin menu options
        print("\n--- Admin Menu ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Add Pet")
        print("4. View Pet Details")
        print("5. Recharge Balance For User")
        print("6. Today's Total Sell")
        print("7. Logout")
        
        choice = input("Enter your choice: ")
        
        try:
            if choice == "1":
                # Display available products
                print("\nAvailable Products:")
                for product in products:
                    print(f"{product['id']}: {product['name']} - ${product['price']}")
                input("Enter any key to continue...")  # Pause to let the admin review

            elif choice == "2":
                # Add a new product to the product list
                product_name = input("Enter product name: ")  # Prompt for product name
                product_price = float(input("Enter product price: "))  # Prompt for product price
                new_id = max(p["id"] for p in products) + 1  # Generate a unique product ID
                products.append({"id": new_id, "name": product_name, "price": product_price})
                print(f"Product '{product_name}' added successfully.")  # Confirmation message
                input("Enter any key to continue...")  # Pause after adding a product

            elif choice == "3":
                # Add a new pet to the system
                name = input("Enter pet name: ")  # Prompt for pet name
                species = input("Enter pet species (Dog/Cat/Bird/Rabbit): ")  # Prompt for species
                age = int(input("Enter pet age: "))  # Prompt for pet age
                additional_data = {}
                # Collect species-specific data
                if species.lower() == "bird":
                    additional_data["wing_span"] = float(input("Enter wing span: "))
                
                elif species.lower() == "rabbit":
                    additional_data["favorite_food"] = input("Enter favorite food: ")
                pet_care_organizer.add_pet(name, species, age, **additional_data)  # Add pet to the organizer
                print(f"Pet '{name}' added successfully.")  # Confirmation message
                input("Enter any key to continue...")  # Pause after adding a pet

            elif choice == "4":
                # View details of a specific pet
                pet_name = input("Enter pet name: ")  # Prompt for pet name
                details = pet_care_organizer.get_pet_details(pet_name)  # Fetch pet details
                if details:
                    print("Pet Details:")  # Display pet details
                    for key, value in details.items():
                        print(f"{key.capitalize()}: {value}")
                
                else:
                    print("Pet not found.")  # Display error if pet does not exist
                input("Enter any key to continue...")  # Pause after viewing pet details

            elif choice == "5":
                # Update the balance of a specific user
                username = input("Enter username to update balance: ")  # Prompt for username
                if username in users:
                    new_balance = float(input("Enter new balance: "))  # Prompt for new balance
                    users[username]["balance"] = new_balance  # Update the user's balance
                    print(f"Balance updated for {username}.")  # Confirmation message
                
                else:
                    print("User not found.")  # Display error if user does not exist
                input("Enter any key to continue...")  # Pause after updating balance
            
            elif choice == "6":
                # Check total ammount of sales for the day
                print(f"Total Sells For Today: {users["admin"]["balance"]}\n")
                input("Enter any key to continue...")  # Pause after checking balance

            elif choice == "7":
                # Exit the admin menu
                break

            else:
                raise ValueError("Invalid choice. Please try again.")  # Raise an exception for invalid input

        except ValueError as e:
            print(e)





#================================================================================================
#================================================================================================
#===========================                          ===========================================
#===========================          Main            ===========================================
#===========================                          ===========================================
#================================================================================================
#================================================================================================


# Main function to start the application
def main():
    while(True):
        print("\nWelcome to Pet House!")
        user = authenticate()
        if user:
            role = users[user]["role"]
            if role == "admin":
                admin_menu()
            
            elif role == "user":
                user_menu(user)

if __name__ == "__main__":
    main()
