from tkinter import *
import random
root=Tk()
root.title("Countries and Capitals")
root.geometry("600x600")

enter_country= Entry(root)
enter_country.place(relx=0.5, rely= 0.2, anchor=CENTER)


enter_capital= Entry(root)
enter_capital.place(relx=0.5, rely= 0.5, anchor=CENTER)

label_capital= Label(root)
label_country= Label(root)

label_country_random= Label(root)
label_capital_random= Label(root)

country_list=[]
capital_list=[]

def add() :
    country_name= enter_country.get()
    country_list.append(country_name)
    
    label_country["text"]= "Country name : " + str(country_list)
    
    capital_name= enter_capital.get()
    capital_list.append(capital_name)
    
    label_capital["text"]= "Capital name : " + str(capital_list)
def random_func():
    length = len(country_list)
    random_country = random.randint(0, length-1)
    random_country1 = country_list[random_country]
    label_country_random["text"]= " Random country = " + random_country1
    length1 = len(capital_list)
    random_cap = random.randint(0, length-1)
    random_cap1 = capital_list[random_cap]
    label_capital_random["text"]= " Random Capital = " + random_cap1

btn1 = Button(root, text="Show capitals and country's list!   ", command =add)
btn1.place(relx= 0.5, rely = 0.7, anchor= CENTER )
btn2 = Button(root, text="Show random capitals and country's list!   ", command =random_func)
btn2.place(relx= 0.5, rely = 0.10, anchor= CENTER )
label_country.place(relx=0.5, rely=0.3, anchor=CENTER) 

label_capital_random.place(relx=0.5, rely=0.1, anchor=CENTER)

label_capital.place(relx=0.5, rely=0.6, anchor=CENTER)

label_country_random.place(relx=0.5, rely=0.8, anchor=CENTER)
root.mainloop()