"""
Data Analysis tool(byt zhuan yong :)

Base on: https://github.com/rdbende/ttk-widget-factory
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import statistics
from collections import Counter
################################# Functions #################################
def update_tree_view():
    global treeview
    row_keys = df.index.tolist()
    # Insert data into Treeviewh
    treeview.delete(*treeview.get_children())
    for i, row_key in enumerate(row_keys):
        values = df.iloc[i].tolist()
        treeview.insert('', 'end', values=values)

def clear_nan():
    global df
    df = df.dropna()
    update_tree_view()

def save_file():
    global df, file_name
    print(file_name[0:-3]+"_processed" + file_name[-3:])
    df.to_csv(file_name[0:-4]+"_processed" + file_name[-4:], index=False)    
################################# End of Functions ################################# 

################################# Variables #################################
file_name = filedialog.askopenfilename()
df = pd.read_csv(file_name)
################################# End of Variables #################################

################################# Data Analysis #################################
mean_values = []
median_values = []
for index, row in df.iterrows():
    # Calculate mean and median excluding the 'Name' column
    mean = row[1:].mean()
    median = row[1:].median()
    mean_values.append(mean)
    median_values.append(median)
# Function to calculate mode for each row
def calculate_mode(row):
    # Exclude the 'Name' column from calculations
    values = row[1:]
    # Count occurrences of each value
    counts = Counter(values)
    # Find the mode(s) and return as a list
    mode = [value for value, count in counts.items() if count == max(counts.values())]
    # If multiple modes, return them as a comma-separated string
    return ','.join(map(str, mode))

# Apply the custom function to each row
df['Mode'] = df.apply(calculate_mode, axis=1)
df['Mean'] = mean_values
df['Median'] = median_values
################################# End of Data Analysis #################################

################################# GUI #################################
root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False) # This is always a good idea

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")

# Create lists for the Comboboxes
option_menu_list = ["", "OptionMenu", "Option 1", "Option 2"]
combo_list = ["Combobox", "Editable item 1", "Editable item 2"]
readonly_combo_list = ["Readonly combobox", "Item 1", "Item 2"]

# Create control variables
a = tk.BooleanVar()
b = tk.BooleanVar(value=True)
c = tk.BooleanVar()
d = tk.IntVar(value=2)
e = tk.StringVar(value=option_menu_list[1])
f = tk.BooleanVar()
g = tk.DoubleVar(value=75.0)
h = tk.BooleanVar()

# Create a Frame for the Checkbuttons
# check_frame = ttk.LabelFrame(root, text="Checkbuttons", padding=(20, 10))
# check_frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10), sticky="nsew")

# # Checkbuttons
# check_1 = ttk.Checkbutton(check_frame, text="Remove All NAN Row", variable=a)
# check_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
# check_2 = ttk.Checkbutton(check_frame, text="Checked", variable=b)
# check_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
# check_3 = ttk.Checkbutton(check_frame, text="Third state", variable=c)
# check_3.state(["alternate"])
# check_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
# check_4 = ttk.Checkbutton(check_frame, text="Disabled", state="disabled")
# check_4.state(["disabled !alternate"])
# check_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# # Separator
# separator = ttk.Separator(root)
# separator.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="ew")

# # Create a Frame for the Radiobuttons
# radio_frame = ttk.LabelFrame(root, text="Radiobuttons", padding=(20, 10))
# radio_frame.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="nsew")

# # Radiobuttons
# radio_1 = ttk.Radiobutton(radio_frame, text="Deselected", variable=d, value=1)
# radio_1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")
# radio_2 = ttk.Radiobutton(radio_frame, text="Selected", variable=d, value=2)
# radio_2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")
# radio_3 = ttk.Radiobutton(radio_frame, text="Mixed")
# radio_3.state(["alternate"])
# radio_3.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")
# radio_4 = ttk.Radiobutton(radio_frame, text="Disabled", state="disabled")
# radio_4.grid(row=3, column=0, padx=5, pady=10, sticky="nsew")

# Create a Frame for input widgets
widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)
# Button
clear_nan_but = ttk.Button(widgets_frame, text="Clear all Nan", command=clear_nan)
clear_nan_but.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

# Button
save_file_but = ttk.Button(widgets_frame, text="Save File", command=save_file)
save_file_but.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

# # Entry
# entry = ttk.Entry(widgets_frame)
# entry.insert(0, "Entry")
# entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew")

# # Spinbox
# spinbox = ttk.Spinbox(widgets_frame, from_=0, to=100)
# spinbox.insert(0, "Spinbox")
# spinbox.grid(row=1, column=0, padx=5, pady=10, sticky="ew")

# # Combobox
# combobox = ttk.Combobox(widgets_frame, values=combo_list)
# combobox.current(0)
# combobox.grid(row=2, column=0, padx=5, pady=10,  sticky="ew")

# # Read-only combobox
# readonly_combo = ttk.Combobox(widgets_frame, state="readonly", values=readonly_combo_list)
# readonly_combo.current(0)
# readonly_combo.grid(row=3, column=0, padx=5, pady=10,  sticky="ew")

# # Menu for the Menubutton
# menu = tk.Menu(widgets_frame)
# menu.add_command(label="Menu item 1")
# menu.add_command(label="Menu item 2")
# menu.add_separator()
# menu.add_command(label="Menu item 3")
# menu.add_command(label="Menu item 4")

# # Menubutton
# menubutton = ttk.Menubutton(widgets_frame, text="Menubutton", menu=menu, direction="below")
# menubutton.grid(row=4, column=0, padx=5, pady=10, sticky="nsew")

# # OptionMenu
# optionmenu = ttk.OptionMenu(widgets_frame, e, *option_menu_list)
# optionmenu.grid(row=5, column=0, padx=5, pady=10, sticky="nsew")

# # Button
# button = ttk.Button(widgets_frame, text="Button")
# button.grid(row=6, column=0, padx=5, pady=10, sticky="nsew")

# # Accentbutton
# accentbutton = ttk.Button(widgets_frame, text="Accentbutton", style="Accent.TButton")
# accentbutton.grid(row=7, column=0, padx=5, pady=10, sticky="nsew")

# # Togglebutton
# button = ttk.Checkbutton(widgets_frame, text="Togglebutton", style="ToggleButton")
# button.grid(row=8, column=0, padx=5, pady=10, sticky="nsew")

# # Switch
# switch = ttk.Checkbutton(widgets_frame, text="Switch", style="Switch")
# switch.grid(row=9, column=0, padx=5, pady=10, sticky="nsew")

# Panedwindow
paned = ttk.PanedWindow(root, width=600)
paned.grid(row=0, column=2, pady=(25, 5), sticky="nsew", rowspan=3)

# Pane #1
pane_1 = ttk.Frame(paned)
paned.add(pane_1, weight=1)
# Create a Frame for the Treeview
treeFrame = ttk.Frame(pane_1)
treeFrame.pack(expand=False, fill="y", padx=5, pady=5)

# Scrollbar
treeScrolly = ttk.Scrollbar(treeFrame)
treeScrolly.pack(side="right", fill="y")
# Scrollbar
treeScrollx = ttk.Scrollbar(treeFrame, orient="horizontal")
treeScrollx.pack(side="bottom", fill="x")
# Treeview
row_count, col_count = df.shape
row_keys = df.index.tolist()
column_keys = df.columns.tolist()
treeview = ttk.Treeview(treeFrame, yscrollcommand=treeScrolly.set, xscrollcommand=treeScrollx.set, columns=column_keys, height=20)
treeview.pack(expand=True, fill="y")
treeScrolly.config(command=treeview.yview)
treeScrollx.config(command=treeview.xview)

# Configure the columns
# For the first column, use special identifier "#0"
treeview.column("#0", width=120)
treeview.heading("#0",anchor="w")
for index, col in enumerate(column_keys):
    # For other columns, use numerical indices starting from 1
    treeview.column(index, anchor="w", width=120)
    treeview.heading(index, text=col, anchor="w")

# Insert data into Treeviewh
for i, row_label in enumerate(row_keys):
    values = df.iloc[i].tolist()
    numeric_values = [x for x in values if isinstance(x, (int, float))]
    treeview.insert('', 'end', values=values)



# # Pane #2
# pane_2 = ttk.Frame(paned)
# paned.add(pane_2, weight=3)

# # Notebook
# notebook = ttk.Notebook(pane_2)

# # Tab #1
# tab_1 = ttk.Frame(notebook)
# tab_1.columnconfigure(index=0, weight=1)
# tab_1.columnconfigure(index=1, weight=1)
# tab_1.rowconfigure(index=0, weight=1)
# tab_1.rowconfigure(index=1, weight=1)
# notebook.add(tab_1, text="Tab 1")

# # Scale
# scale = ttk.Scale(tab_1, from_=100, to=0, variable=g, command=lambda event: g.set(scale.get()))
# scale.grid(row=0, column=0, padx=(20, 10), pady=(20, 0), sticky="ew")

# # Progressbar
# progress = ttk.Progressbar(tab_1, value=0, variable=g, mode="determinate")
# progress.grid(row=0, column=1, padx=(10, 20), pady=(20, 0), sticky="ew")

# # Label
# label = ttk.Label(tab_1, text="Forest ttk theme", justify="center")
# label.grid(row=1, column=0, pady=10, columnspan=2)

# # Tab #2
# tab_2 = ttk.Frame(notebook)
# notebook.add(tab_2, text="Tab 2")

# # Tab #3
# tab_3 = ttk.Frame(notebook)
# notebook.add(tab_3, text="Tab 3")

# notebook.pack(expand=True, fill="both", padx=5, pady=5)

# Sizegrip
sizegrip = ttk.Sizegrip(root)
sizegrip.grid(row=100, column=100, padx=(0, 5), pady=(0, 5))

# Center the window, and set minsize
root.update()
root.minsize(root.winfo_width(), root.winfo_height())
x_cordinate = int((root.winfo_screenwidth()/2) - (root.winfo_width()/2))
y_cordinate = int((root.winfo_screenheight()/2) - (root.winfo_height()/2))
root.geometry("+{}+{}".format(x_cordinate, y_cordinate))

# Start the main loop
root.mainloop()
################################# End of GUI #################################

