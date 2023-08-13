import json

# Function to load tasks from a JSON file
def load_tasks():
    try:
        with open("-8tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to display tasks
def display_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index}. {task['title']} - {task['description']} - {status}")

# Function to add a new 


def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    tasks.append({"title": title, "description": description, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to mark a task as done
def mark_done(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter the task number to mark as done: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Application")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
