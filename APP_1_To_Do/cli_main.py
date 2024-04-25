# user_prompt = "Enter a To Do: "
# user_text = input(user_prompt)
# print(user_text)

# str (immutable) methods: capitalize, title, upper, replace(org, rep[, inst]),split()
# list (mutable) methods: append, index(search), __setitem__(i, rep), __getitem__(i). sort([reverse=])
# dict.values() = vals as list
# list = [] ; tuple = (); dict = {}
# while cond:
# ==, !=
# functions: len, type, print, input, int, float, str, zip = return tuple, all = list all true?, exit

# console: dir(object), help(object[.method]), import builtins -> dir(builtins)
# csv, json for complex data; sql for extremely complex input
# write/read for str; writelines/readlines for lists
# r"" - ignore special char. f""
# /Users/user/path - absolute path
#  split string \, split list with commas
# """"""" = multi-line strings


# todos = []

# import functions; from dir.file
# important modules glob .glob("*.txt"); csv list(csv.reader(file));
# shutil = shell utility .make_archive(out, zip, dir); webbrowser .open("https://{str}.com/search?q=")
# json .load(json content)

from functions import *
import time

time_var = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {time_var}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        # td = input("Enter a To Do: ") + '\n'

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)
    elif user_action.startswith('show') or user_action.startswith('display'):
        todos = get_todos()

        todos = [item.strip('\n') for item in todos]
        for i, item in enumerate(todos):
            # item = item.title()
            print(f"{i + 1}. {item}")
    elif user_action.startswith('edit'):
        try:
            # num = int(input("Number of To Do to Edit: "))
            num = int(user_action[5:]) - 1

            todos = get_todos()

            todos[num] = input("Enter New To Do: ") + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            del_item = int(input(user_action[9:]))
            index = del_item - 1

            todos = get_todos()

            todo_rm = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"To Do {todo_rm} was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("Unknown Command!")
    # case _:
    #     print("Unknown Command!")

print("Bye!")