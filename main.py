from tkinter import *
from tkinter import ttk #need to import for Combobox(Dropdown)

def calcu(): #Calculation of BMI
    #need to try converting input from entry(comment box) to float first 
    try:    
        kg =float(weight_entry.get()) 
        m = float(height_entry.get())
    #if the user entered a value that is not a int or float except ValueError will execute and end the function
    except ValueError: 
        bmi.config(text="BMI: Wrong Inputs")
        return
    
    #Conversion of units to kg and m depending on the chosen unit
    if x.get() == "lb":
        kg = kg * 0.453592
    elif x.get() == "kg":
        pass
    #else will execute if a unit is not selected in the Combobox
    else: 
        bmi.config(text="BMI: Need units")
        return
        
    if y.get() == "m":
        pass
    elif y.get() == "cm":
        m = m / 100
    elif y.get() == "in":
        m = m / 39.37
    else:
        bmi.config(text="BMI: Need units ") 
        return
    
    #After all that BMI will be calculated using these two formula     
    m = m ** 2   
    results = kg/m    
    
    #this config will overwrite the label BMI with the result
    bmi.config(text=f"BMI: {results:.2f}")

window = Tk()
window.title("BMI Calculator")

#StringVar() is a FUNCTION(in tkinter) that is used to edit a widget's text. (sabi sa stackoverflow)  
x = StringVar() 
y = StringVar()

frame = Frame(window,padx=10,pady=10) 
frame.pack(side="left")

#Info Frame
info_frame = LabelFrame(frame, text="BMI Calculator")
info_frame.grid(row=0, column=0)

#Weight Section
weight_label = Label(info_frame, text="Weight",padx=40)
weight_label.grid(row=0, column=0)
weight_entry = Entry(info_frame)
weight_entry.grid(row=0, column=1)
weight_combobox = ttk.Combobox(info_frame, 
                               value=["kg","lb"], 
                               textvariable=x)
weight_combobox.grid(row=0,column=2)

#Height Section
height_label = Label(info_frame, text="Height",padx=40)
height_label.grid(row=2, column=0)
height_entry = Entry(info_frame)
height_entry.grid(row=2, column=1)
height_combobox = ttk.Combobox(info_frame, 
                               value=["cm","m","in",], 
                               textvariable=y)
height_combobox.grid(row=2,column=2)

#Calculate Button
calculate = Button(info_frame, 
                   text="Calculate",
                   command=calcu)
calculate.grid(row= 3, column=1) 

#Results
bmi = Label(info_frame, text="BMI:")
bmi.grid(row=4,column=1)

for widget in info_frame.winfo_children(): #for clarity
    widget.grid_configure(padx=10, pady=5) 
    

window.mainloop()    