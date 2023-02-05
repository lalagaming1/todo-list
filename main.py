#Importing GooeyPie module and os module(Operating System)
import gooeypie as gp
import os

#Defining functions
def add_new_task(event):
    """Adds a new task from when the Enter/Return key is pressed"""
    if event.key['name'] == 'Return' and new_task_inp.text != "":
        todo_lst.add_item(new_task_inp.text)
        new_task_inp.clear()
        new_task_inp.focus()

def move_task(event):
    """Moves a task from one listbox to another"""
    if event.widget == todo_lst:
        # move the task from the todo list to the done list
        done_lst.add_item(todo_lst.remove_selected())
    else:
        # move the task back from the done list to the todo list
        todo_lst.add_item(done_lst.remove_selected())

def delete_task(event):
    """Deletes a task from the todo list"""
    todo_lst.remove_selected()
    new_task_inp.focus()

def all_done(event):
    """Moves all tasks from the todo list to the done list"""
    done_lst.items += todo_lst.items
    todo_lst.items = []

def clear_all(event):
    """Remove all tasks from the done list"""
    done_lst.items = []

def load_tasks():
    """"Loads tasks from the tasks file and populates the todo and done listboxes"""
    try:
        with open("tasks.txt") as tasks_file:
            tasks = tasks_file.readline()
        if tasks[0] != "\n":
            todo_lst.items(tasks[0].strip().split("\t"))
        if tasks[1] != "\n":
            done_lst.items(tasks[1].strip().split("\t"))
    except FileNotFoundError:
        pass
    except IndexError:
        #If the file is not of the correct format, inform the user
        message = "The tasks file could not be loaded because it is not in the correct format\n\n Are you sure you want to exit?"
        app.alert("Could not load tasks file", message, "info")
def save_tasks():
    """Saves the todo and done lists to the tasks file"""
    todos = "\t".join(todo_lst.items)
    dones = "\t".join(done_lst.items)
    try:

        with open("tasks.txt", "w") as tasks_file:
            tasks_file.write(f"{todos}\n{dones}\n")
        
    except PermissionError:
        #Inform the user of the error and seek confirmation to exit
        message = f"Could not save tasks file in {os.getcwd()} due to a permision error"
        app.confirm_yesno("Cannot save tasks file", message, "warning")
    return True
#Initializing GooeyPie
app = gp.GooeyPieApp('Todo list')
app.width = 400
#Making the app not resizable
app.set_resizable(False)

# Creating widgets(label, listboxes, input, etc..)
new_task_lbl = gp.Label(app, 'New task')
new_task_inp = gp.Input(app)
todo_lbl = gp.Label(app, 'Todo list')
todo_lst = gp.Listbox(app)
delete_task_btn = gp.Button(app, 'Delete task', delete_task)
all_done_btn = gp.Button(app, 'All done!', all_done)
done_lbl = gp.Label(app, 'Done!')
done_lst = gp.Listbox(app)
clear_all_btn = gp.Button(app, 'Clear all', clear_all)

# Setting up Event Listeners(that lisen for mouse clicks, keyboard presses, etc..)
new_task_inp.add_event_listener('key_press', add_new_task)
todo_lst.add_event_listener('double_click', move_task)
done_lst.add_event_listener('double_click', move_task)

# Add widgets to window and setting grid which is used for placing widgets on window
app.set_grid(5, 3)
app.set_column_weights(0, 1, 1)
app.set_row_weights(0, 1, 0, 1, 0)
app.add(new_task_lbl, 1, 1, align='right')
app.add(new_task_inp, 1, 2, column_span=2, fill=True)
app.add(todo_lbl, 2, 1, align='right')
app.add(todo_lst, 2, 2, column_span=2, fill=True, stretch=True)
app.add(delete_task_btn, 3, 2, fill=True)
app.add(all_done_btn, 3, 3, fill=True)
app.add(done_lbl, 4, 1, align='right')
app.add(done_lst, 4, 2, column_span=2, fill=True, stretch=True)
app.add(clear_all_btn, 5, 3, fill=True)
#Load tasks from the tasks file
app.on_open(load_tasks)
#Save Tasks
app.on_close(save_tasks)
#Focusing on the new task input box to quickly add tasks to the todo list
new_task_inp.focus()
#Running the app
app.run()