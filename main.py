import csv
import random

def add_person(file_path, name, surname):
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname])

def get_random_person(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        persons = list(reader)

    if len(persons) > 0:
        return random.choice(persons)
    else:
        return None

def main():
    file_path = 'users.csv'

    while True:
        print("\nOptions:")
        print("1. Add a person")
        print("2. Get a random person")
        print("3. Quit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            name = input("Enter the person's name: ")
            surname = input("Enter the person's surname: ")
            add_person(file_path, name, surname)
            print("Person added successfully!")

        elif choice == '2':
            random_person = get_random_person(file_path)
            if random_person:
                print("Random person: {} {}".format(random_person[0], random_person[1]))
            else:
                print("No persons in the file. Add a person first.")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()