import json


# Function to add a new person to the contact list
def add_person():
    # Prompt the user for name, age, and email of the new person
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    # Create a dictionary for the new person and return it
    person = {"name": name, "age": age, "email": email}
    return person


# Function to display all people in the contact list
def display_people(people):
    # Loop through all people and display their details
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


# Function to delete a contact from the list
def delete_contact(people):
    # Show all the contacts before asking for deletion
    display_people(people)

    while True:
        # Ask the user for the number of the contact to delete
        number = input("Enter a number to delete: ")
        try:
            # Convert input to an integer and check if it's valid
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number out of range.")  # Notify if the number is invalid
            else:
                break  # Break the loop if the number is valid
        except:
            # Handle invalid inputs
            print("Invalid number.")

    # Remove the selected person from the list
    people.pop(number - 1)
    print("Person deleted.")  # Notify the user that the person was deleted


# Function to search for contacts by name (case-insensitive)
def search(people):
    # Ask the user for a name to search
    search_name = input("Search for a name: ").lower()
    results = []

    # Loop through the people list and check if the search term matches the name
    for person in people:
        name = person["name"]
        if search_name in name.lower():  # Case-insensitive comparison
            results.append(person)  # Add matching people to results

    # Display the search results
    display_people(results)


# Main part of the program
print("Hi, welcome to the Contact Management System.")
print()

# Load existing contacts from the 'contacts.json' file
with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

# Main loop to keep the program running until the user decides to quit
while True:
    print()
    print("Contact list size:", len(people))  # Display the current number of contacts
    # Prompt the user for a command
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        # Add a new contact if the user chooses 'add'
        person = add_person()
        people.append(person)
        print("Person added!")  # Notify the user that the person was added
    elif command == "delete":
        # Delete an existing contact if the user chooses 'delete'
        delete_contact(people)
    elif command == "search":
        # Search for a contact if the user chooses 'search'
        search(people)
    elif command == "q":
        # Exit the program if the user chooses 'q'
        break
    else:
        # Handle invalid commands
        print("Invalid command.")

# Save the updated contacts list back to the 'contacts.json' file
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)
