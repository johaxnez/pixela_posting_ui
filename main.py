# Pixela link : https://pixe.la/v1/users/johaxnez/graphs/graph1.html

import requests
import datetime
from tkinter import *
from tkinter import messagebox

root = Tk()

pixela_endpoint = "https://pixe.la/v1/users"
PIXELA_USERNAME = "USER- private"
PIXELA_TOKEN = "TOKEN - private"
GRAPH_ID = "graph1"
user_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfservice" : "yes",
    "notMinor": "yes",
}


headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}


today = datetime.datetime.today()


####################--Functions --############################
date_today = ""
def format_date():
    global date_today
    date_today = today.strftime("%Y%m%d")
    date_input.delete(0, END)
    date_input.insert(0, date_today)
    return date_today

def post_minutes():
    parameters = {
        "date": str(str(date_input.get())),
        "quantity": str(minutes_coded.get()),
    }
    if len(minutes_coded.get()) == 0:
        messagebox.showerror("error", "Please insert the minutes you have coded")
    else:
        try:
            response = requests.post(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}", json=parameters,
                                     headers=headers)
            messagebox.showinfo("Success", "Your time was posted")
        except requests.exceptions.HTTPError:
            messagebox.showerror("error", "insert valid date")
        finally:
            print(response.text)
        print(type(response.text))



def delete_post():
    try:
        response = requests.delete(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{str(date_input.get())}",
                                   headers=headers)
        response.raise_for_status()
        messagebox.showinfo("Success", "Your post was deleted")
    except requests.exceptions.HTTPError:
        messagebox.showerror("error", "insert valid date")
    finally:
        print(response.text)


def update():
    put_params = {
        "quantity": str(update_minutes_coded.get()),
    }
    if len(update_minutes_coded.get()) == 0:
        messagebox.showerror("error", "Please insert the updated minutes")
    else:
        try:
            response = requests.put(url=f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{str(date_input.get())}",
                                    json=put_params, headers=headers)
            response.raise_for_status()
            messagebox.showinfo("success", "Your post was updated")
        except requests.exceptions.HTTPError:
            messagebox.showerror("error", "insert valid date")
        finally:
            print(response.text)



####################--User UI--###############################
root.geometry("750x350")
root.title("Code tracker")


date_label = Label(text="Write the date you wish to post/update/delete", font=("Arial", 20, "bold"))
date_label.grid(row=0, column=0, columnspan=2)

info_label = Label(text="Input the minutes you have coded today.", font=("Arial", 20, "bold"))
info_label.grid(row=3, column=0, columnspan=2, padx=10)

update_label = Label(text="Update input for a given day", font=("Arial", 20, "bold"))
update_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

delete_label = Label(text="Push delete to delete the input at a given date.", font=("Arial", 20, "bold"))
delete_label.grid(row=10, column=0, columnspan=2)

date_input = Entry(width=35)
date_input.insert(0, "yyyyMMdd")
date_input.grid(row=1, column=0, padx=10)

minutes_coded = Entry(width=35)
minutes_coded.grid(row=4, column=0, padx=10)

post_button = Button(text="Post to Pixela", width=30, command=post_minutes)
post_button.grid(row=6, column=0, padx=10)

update_button = Button(text="Update", command=update, width=30)
update_button.grid(row=9, column=0)

delete_button = Button(text="Delete", bg="red", width=30, command=delete_post)
delete_button.grid(row=11, column=0)

date_is_today = Button(text="Todays day", command=format_date, width=35)
date_is_today.grid(row=1, column=1)

update_minutes_coded = Entry(width=35)

update_minutes_coded.grid(row=8, column=0)




root.mainloop()