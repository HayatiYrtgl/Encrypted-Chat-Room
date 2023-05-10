import json
import tkinter as tk
from tkinter import messagebox
from functools import partial


# creating dictionary to save as a json file

configuration_file_json = {"username": "",
                           "port": 80,
                           "host": "", }

# saving file and ive message


def saving_file(configuration_to_save, username_gui, port_gui, host_gui, btn_object):
    # catch errors with try except
    try:
        # configure the json with gui inputs

        configuration_to_save["username"] = username_gui.get()

        configuration_to_save["port"] = int(port_gui.get())

        configuration_to_save["host"] = host_gui.get() + ".tcp.eu.ngrok.io"

        # create file if exists reset it and create again

        with open("config_file/configuration.json", "w") as file:

            json.dump(configuration_to_save, file, ensure_ascii=False, indent=4)

            messagebox.showinfo("BİLGİ", "Dosya Kaydedildi")

            # if process is completed successfully set button disable

            btn_object.config(state="disabled")

    except ValueError:
        messagebox.showerror("HATA", "Port Numarası sayı olmalıdır")

# tkinter side

# create window


login = tk.Tk()

# window configurations

login.title("Login Page")

login.geometry("450x200+450+190")

login.config(bg="gray12")

# labels of window

# window main label

main_label = tk.Label(login, text="LOGIN CONFIGURATION", font=("Mesquite Std", 35), fg="green", bg="gray12")

main_label.grid(row=0, column=2)

# username label and entry

username = tk.Label(login, text="Kullanıcı Adı :", font=("Times New Roman", 13), fg="red", bg="gray12")

username.grid(row=1, column=1, sticky="W", pady=10)

"""username entry"""

username_entry = tk.Entry(login)

username_entry.grid(row=1, column=2)

# port label and entry

port = tk.Label(login, text="Port :", font=("Times New Roman", 13), fg="red", bg="gray12")

port.grid(row=2, column=1, sticky="W", pady=10)

"""port entry"""

port_entry = tk.Entry(login)

port_entry.grid(row=2, column=2)

# host label and entry

host = tk.Label(login, text="Host :", font=("Times New Roman", 13), fg="red", bg="gray12")

host.grid(row=3, column=1, sticky="W", pady=10)

"""host spinbox"""

# spinbox current value

current_value = tk.StringVar(value="0")

host_entry = tk.Spinbox(login, from_=0, to=7, wrap=True, textvariable=current_value, width=18)

host_entry.grid(row=3, column=2)

# button section and configurating command with partial pass arg

save_conf_button = tk.Button(login, text="Kaydet", width=13, borderwidth=8)

# set command the button

save_conf_button.config(command=partial(saving_file, configuration_file_json, username_entry, port_entry, host_entry,
                                        save_conf_button))

save_conf_button.grid(row=3, column=3, padx=5)


login.mainloop()
