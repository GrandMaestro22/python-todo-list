def main():
    todo_items = []

    while True:
        task = input("Enter your task: ")
        todo_items.append(task)
        print("Current To-Do List:")
        for index, item in enumerate(todo_items, start=1):
            print(f"{index}. {item}")
        
        choice = input("What would you like to do next? (add/remove/exit): ").strip().lower()
        if choice == "add":
            continue
        elif choice == "remove":
            try:
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(todo_items):
                    removed_task = todo_items.pop(task_number - 1)
                    print(f"Removed task: {removed_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "exit":
            print("Exiting the To-Do List application. Goodbye!")
            break

main()