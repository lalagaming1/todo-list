#Importing GooeyPie Module
import gooeypie as gp
#Defining Functions
def Delete_Task():
    Tasks_lsb.selected = Tasks_lsb.selected - Tasks_lsb.items


def clear_all():
    Tasks_lsb.items = []



#Initializing GooeyPie and window properties(width, resizabilty, etc..)
app = gp.GooeyPieApp("Todo-list")
app.width = 400
app.set_resizable = False
#Creating Widgets(labels, listboxes, input, etc..)
New_Task_lbl = gp.Label(app, "New Task")
New_Task_lsb = gp.Input(app)
Tasks_lbl = gp.Label(app, "Tasks")
Tasks_lsb = gp.Listbox(app)
Delete_Task_btn = gp.Button(app, "Delete Task", Delete_Task)
Clear_All_btn = gp.Button(app, "Clear All", clear_all)
#Setting grid and Placing widgets on window(Setting Grid is used to place widgets on window)
app.set_grid(5,3)
app.add(New_Task_lbl, 1, 1)
app.add(New_Task_lsb, 1, 2)
app.add(Tasks_lbl, 2, 1)
app.add(Tasks_lsb, 2, 2)
app.add(Clear_All_btn, 3, 1)
app.add(Delete_Task_btn, 3, 2)
#Running Application
app.run()
