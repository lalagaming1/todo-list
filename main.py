#Importing GooeyPie Module
import gooeypie as gp

#Initializing GooeyPie and window properties
app = gp.GooeyPieApp("Todo-list")
app.width = 400
app.set_resizable = False
#Creating Widgets
New_Task_lbl = gp.Label(app, "New Task")
New_Task_lsb = gp.Listbox(app)
Tasks_lbl = gp.Label(app, "Tasks")
Tasks_lsb = gp.Listbox(app)
Delete_Task_btn = gp.Button(app, "Delete Task", None)
Clear_All_btn = gp.Button(app, "Clear All", None)
#Setting grid and Placing widgets on window
app.set_grid(5,3)
app.add(New_Task_lbl, 1, 1)
app.add(New_Task_lsb, 1, 2)
app.add(Tasks_lbl, 2, 1)
app.run()
