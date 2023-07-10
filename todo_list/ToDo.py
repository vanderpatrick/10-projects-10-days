def main():
    dict_of_items = {1: 'study', 2: 'eat'}
    print("Welcome to your todo list. Choose the options below to manage your list:")
    print("1: Check your list")
    print("2: Add an item")
    print("3: Delete an item")

    while True:
        user_input = input('Select an option: ')

        try:
            option = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid option.")
            continue

        if option == 1:
            if not dict_of_items:
                print("List is empty")
            else:
                for item_id, item_text in dict_of_items.items():
                    print(f"{item_id}: {item_text}")

        elif option == 2:
            item_input = input("What do you need to do? ")
            add_item(dict_of_items, item_input)
            print(dict_of_items)

        elif option == 3:
            print(dict_of_items)
            delete_input = input("What do you want to delete? ")

            try:
                del_input = int(delete_input)
                delete_item(dict_of_items, del_input)
                print(f"You deleted item with ID {del_input}")
            except ValueError:
                print("Invalid input. Please enter a valid option.")
            else:
                print(f"You deleted item with ID {delete_input}")
                print(dict_of_items)

        else:
            print("Invalid option. Please choose a valid option.")
            continue

        if input("Do you want to continue? (Y/N): ").lower() != 'y':
            break


def add_item(dict_of_items, item_input):
    item_id = len(dict_of_items) + 1
    dict_of_items[item_id] = item_input


def delete_item(dict_of_items, item_id):
    dict_of_items.pop(item_id, None)



if __name__ == "__main__":
    main()