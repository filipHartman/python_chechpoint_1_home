import os.path


def check_file_in_dir():
    if not os.path.exists("todo.txt"):
        f = open("todo.txt", "w")
        f.close()


def choose_action(choice):
    choice = choice.upper()
    if choice == "LIST":
        list_tasks()
    elif choice == "ADD":
        add_task()
    elif choice == "MARK":
        mark_as_completed()
    elif choice == "ARCHIVE":
        archive_completed_tasks()
    else:
        exit()


def list_tasks():
        print("\nYou saved the following to-do items: \n")
        with open("todo.txt", "r") as todo_file:
            for line in todo_file:
                print("  ", line)


def check_number_of_tasks():
    with open("todo.txt", "r") as todo_file:
        counter = 0
        if not os.path.getsize("todo.txt"):
            return counter
        else:
            for line in todo_file:
                counter += 1
            return counter


def add_task():
    task = input("Add an item: ").lower()
    if task[0].islower():
        task = task[0].upper() + task[1:]

    lines_in_file = check_number_of_tasks()
    number = str(lines_in_file + 1)

    with open("todo.txt", "a") as todo_file:
        task_file = number + ". [ ] " + task + "\n"
        todo_file.write(task_file)
    print("Item added.")


def mark_as_completed():
    list_tasks()
    task_to_mark = int(input("Which one you want to mark as completed: "))
    task_to_mark -= 1

    with open("todo.txt", "r") as todo_file:
        tasks = todo_file.readlines()
        task = tasks[task_to_mark].replace("[ ]", "[x]")
        tasks[task_to_mark] = task

    with open("todo.txt", "w") as todo_file:
        for item in tasks:
            todo_file.write(item)

        task = task.split("]")
        print("{} is completed".format(task[1].strip(" \n")))


def archive_completed_tasks():
    with open("todo.txt", "r") as todo_file:
        tasks = todo_file.readlines()
        undone_tasks = []
        for item in tasks:
            if "[x]" not in item:
                undone_tasks.append(item)

        for index in range(len(undone_tasks)):
            if int(undone_tasks[index][0]) != index + 1:
                updated_task = str(index + 1) + undone_tasks[index][1:]
                undone_tasks[index] = updated_task

    with open("todo.txt", "w") as todo_file:
        for item in undone_tasks:
            todo_file.write(item)

    print("All completed tasks got deleted.")


def main():
    check_file_in_dir()
    choice = input("Please specify a command [list, add, mark, archive]: ")
    choose_action(choice)


main()
