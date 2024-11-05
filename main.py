# Simple To-Do List Program

# Load the tasks from the file
def load_tasks(filename="todo.txt"):
    """
    Reads tasks from a specified file and returns them as a list.
    Each line in the file represents a task.
    """
    with open(filename, "r") as file:
        return [line.rstrip('\n') for line in file]


# Save the tasks to the file
def save_tasks(tasks, filename="todo.txt"):
    """
    Writes the list of tasks back to the file.
    """
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Display the tasks to the user
def display_tasks(tasks):
    """
    Prints all tasks with their status markers.
    Returns a list mapping displayed task numbers to their indices in 'tasks'.
    """
    print("\nYour to-do list:")
    task_indices = []
    for idx, task in enumerate(tasks):
        print(f"{idx + 1} {task}")
        task_indices.append(idx)
    return task_indices


# Main function
def main():
    # Load tasks from the file
    try:
        tasks = load_tasks()
    except FileNotFoundError:
        tasks = []

    # Display welcome message and instructions
    print("Welcome to simple-to-dos!")
    print("* Enter the task number to mark it as complete,")
    print("* Hit enter on an empty line to quit, or")
    print("* Write some text to add a new task.")

    while True:
        # Show all tasks and get mapping of displayed numbers to task indices
        task_indices = display_tasks(tasks)

        # Get user input
        user_input = input("Your input >> ").strip()

        if user_input == "":
            # Exit the loop if input is empty (user wants to quit)
            break

        elif user_input.isdigit():
            # If input is a number, map it to the correct task index
            user_choice = int(user_input)
            if 1 <= user_choice <= len(task_indices):
                task_index = task_indices[user_choice - 1]
                # Mark the task as complete if it's not already
                if tasks[task_index].startswith("-"):
                    tasks[task_index] = "x" + tasks[task_index][1:]
                else:
                    print("That task is already completed.")
            else:
                print("Invalid task number.")

        else:
            # If input is not a number, treat it as a new task
            tasks.append(f"- {user_input}")  # Add new task with '-' prefix

    # Save updated tasks back to the file before exiting
    save_tasks(tasks)
    print("Your tasks have been updated. Goodbye!")


# Run the program
if __name__ == "__main__":
    main()