shopping_list = list()


def show_help():
    print("What shoud we pick up at the store?")
    print("Enter DONE to stop. And enter HELP for this help.")
    print("Enter SHOW to show the current list")


def add_to_list(item):
    shopping_list.append(item)
    print("Added! {} itens in your list!".format(len(shopping_list)))


def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)


show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        if len(shopping_list) == 0:
            print("You didn't add itens yet!")
            continue
        else:
            show_list()
        continue

    add_to_list(new_item)
    continue

show_list()
