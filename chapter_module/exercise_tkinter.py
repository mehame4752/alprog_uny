from tkinter import *
from tkinter import ttk

# todo:
# classify bmi value
# documentation of code

calculation_method = ['metric', 'imperial']

relation_mass_calculate = dict(zip(calculation_method, ['Kg', 'Lbs']))
relation_height_calculate = dict(zip(calculation_method, ['Meter', 'Inch']))

def selection_changed(event):
    calculation_based = based_calculate.get()
    height_text.set(
        relation_height_calculate[calculation_based]
    )
    mass_text.set(
        relation_mass_calculate[calculation_based]
    )

# weight in kg, weight in meter
calculate_bmi_metric = lambda weight, height: weight / (height**2)

# weight in lbs, height in inch
calculate_bmi_imperial = lambda weight, height: 730 * weight / (height**2)

relation_calculator_bmi = dict(zip(calculation_method, [calculate_bmi_metric, calculate_bmi_imperial]))

def calculate(*args):
    try:
        weight_val = float(mass.get())
        height_val = float(height.get())

        method_calculation = based_calculate.get()

        result = relation_calculator_bmi[method_calculation](
            weight=weight_val,
            height=height_val
        )

        bmi_value.set(result)
    except ValueError:
        bmi_value.set('error ocurred when calculation')

root = Tk()
root.title("BMI Calculator")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=100)
root.rowconfigure(0, weight=1)

mass = StringVar()
mass_entry = ttk.Entry(mainframe, width=10, textvariable=mass)
mass_entry.grid(column=2, row=2, sticky=(W, E))

mass_text = StringVar(value='Kg')
ttk.Label(mainframe, textvariable=mass_text).grid(column=3, row=2, sticky=(W, E))

height = StringVar()
height_entry = ttk.Entry(mainframe, width=10, textvariable=height)
height_entry.grid(column=2, row=3, sticky=(W, E))

height_text = StringVar(value='Meter')
ttk.Label(mainframe, textvariable=height_text).grid(column=3, row=3, sticky=(W, E))

based_calculate = ttk.Combobox(
    values=calculation_method,
)
based_calculate.place(x=130, y=8, width=100)
based_calculate.bind("<<ComboboxSelected>>", selection_changed)
based_calculate.set(calculation_method[0])

bmi_value = StringVar(value='')
ttk.Label(mainframe, textvariable=bmi_value).grid(column=2, row=6, sticky=E)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=4, sticky=W, rowspan=2)

ttk.Label(mainframe, text="Calculated based").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Mass").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="Height").grid(column=1, row=3, sticky=W)

ttk.Label(mainframe, text="Your BMI: ").grid(column=1, row=6, sticky=E)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

mass_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()