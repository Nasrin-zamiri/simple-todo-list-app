def print_list(todo_list):
    if len(todo_list) == 0:
        print("empty list")
    for index, item in enumerate(todo_list):
        print(f"{index + 1}. {item}")


def get_list(todo_list):
    list = ""
    for index, item in enumerate(todo_list):
        list += f"{index + 1}. {item}\n"
    return list


def main():
    todo_list = []
    option = 0
    while option != "4":
        option = input("enter an option from the following:\n"
                       "1. view the current todo list\n"
                       "2. add a todo list item\n"
                       "3. remove a todo list item\n"
                       "4. exit the program\n:")
        if option == "1":
            print_list(todo_list)
        if option == "2":
            item = input("enter an item to the list: ")
            todo_list.append(item)
        if option == "3":
            item_to_remove = input(f"enter the number you want to remove?\n{get_list(todo_list)} ")
            if int(item_to_remove) <= len(todo_list):
                todo_list.pop(int(item_to_remove) - 1)
                print_list(todo_list)
            else:
                print("that option doesn't exist")


if __name__ == "__main__":
    main()