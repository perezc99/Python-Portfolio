from functions import *
import tkinter as tk
from tkinter import messagebox
from time import strftime
import os


def check_files():
    if not os.path.exists("I_TM.txt"):
        with open("I_TM.txt", 'w'):
            pass
    if not os.path.exists("NI_TM.txt"):
        with open("NI_TM.txt", 'w'):
            pass
    if not os.path.exists("I_NTM.txt"):
        with open("I_NTM.txt", 'w'):
            pass
    if not os.path.exists("NI_NTM.txt"):
        with open("NI_NTM.txt", 'w'):
            pass

class WindowFrame(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent)

        arg_dict = {}
        for key, val in kwargs.items():
            arg_dict[key] = val

        if arg_dict["pack_or_grid"] == "pack":
            self.pack()
        elif arg_dict["pack_or_grid"] == "grid":
            self.grid(row=int(arg_dict["grid_row"]), column=int(arg_dict["grid_column"]))


class CreateButton:
    def __init__(self, parent, **kwargs):
        arg_dict = {}
        for key, val in kwargs.items():
            arg_dict[key] = val

        self.btn = tk.Button(parent, text=arg_dict["btn_txt"], command=arg_dict["btn_cmd"])
        self.btn.grid(row=arg_dict['r'], column=arg_dict['c'])


class CreateLabel:
    def __init__(self, parent, lbl_text):
        self.lbl = tk.Label(parent, text=lbl_text)
        self.lbl.grid()


class CreateBox:
    def __init__(self, parent):
        self.scroll = tk.Scrollbar(parent)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(parent, yscrollcommand=self.scroll.set)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.config(command=self.listbox.yview)


class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.config(background="black")
        self.title("To Do Application")
        # self.geometry("1000x1000")

        self.whole_frame = WindowFrame(self, pack_or_grid="pack")
        self.tit_frame = WindowFrame(self.whole_frame, pack_or_grid="grid", grid_row=0, grid_column=0)
        self.top_frame = WindowFrame(self.whole_frame, pack_or_grid="grid", grid_row=1, grid_column=0)
        self.mid_frame = WindowFrame(self.whole_frame, pack_or_grid="grid", grid_row=2, grid_column=0)
        self.btm_frame = WindowFrame(self.whole_frame, pack_or_grid="grid", grid_row=3, grid_column=0)

        self.whole_frame.pack_configure(fill=tk.BOTH, expand=True)
        self.whole_frame.columnconfigure(0, weight=10)
        self.whole_frame.rowconfigure(0, weight=1)
        self.whole_frame.rowconfigure(1, weight=1)
        self.whole_frame.rowconfigure(2, weight=1)
        self.whole_frame.rowconfigure(3, weight=100)

        self.btm_frame.rowconfigure(0, weight=33)
        self.btm_frame.rowconfigure(1, weight=33)
        self.btm_frame.rowconfigure(2, weight=33)
        self.btm_frame.columnconfigure(1, weight=40)
        self.btm_frame.columnconfigure(2, weight=40)


        self.tit_time()
        self.build_top_frame()
        self.build_mid_frame()
        self.build_btm_frame()

        self.load_todo()

        self.entry_box.bind("<Return>", func=lambda x: self.add_todo())

    def tit_time(self):
        self.time_text = tk.Label(self.tit_frame)
        self.time_str = strftime("%b %d, %Y %H:%M:%S")
        self.time_text.config(text=self.time_str)
        self.time_text.after(1000, self.tit_time)

    def build_top_frame(self):
        self.top_text = CreateLabel(self.top_frame, lbl_text="Enter To Do: ")
        # .Label(self.top_frame, text="Type To Do: ", bg="#50727B", fg="white")
        # self.window_top_text.grid(row=0)

        self.entry_box = tk.Entry(self.top_frame)
        self.entry_box.grid(row=0, column=1, sticky=tk.NSEW)

        self.chk1_int = tk.IntVar()
        self.chk1 = tk.Checkbutton(self.top_frame, text="Important", variable=self.chk1_int)
        self.chk1.grid(row=0, column=2, sticky=tk.W)

        self.chk2_int = tk.IntVar()
        self.chk2 = tk.Checkbutton(self.top_frame, text="Time-Sensitive", variable=self.chk2_int)
        self.chk2.grid(row=0, column=3, sticky=tk.W)

    def build_mid_frame(self):
        self.add_btn = CreateButton(self.mid_frame, btn_txt="Add", btn_cmd=lambda: self.add_todo(), r=0, c=0)
        self.edit_btn = CreateButton(self.mid_frame, btn_txt="Edit", btn_cmd=lambda: self.edit_todo(), r=0, c=1)
        self.del_btn = CreateButton(self.mid_frame, btn_txt="Delete", btn_cmd=lambda: self.del_todo(), r=0, c=2)
        self.save_btn = CreateButton(self.mid_frame, btn_txt="Save", btn_cmd=lambda: self.save_todo(), r=0, c=4)
        self.exit_btn = CreateButton(self.mid_frame, btn_txt="Exit", btn_cmd=lambda: self.exit_todo(), r=0, c=5)

    def build_btm_frame(self):
        self.top_left = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=0, grid_column=0)
        self.top_mid = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=0, grid_column=1)
        self.top_right = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=0, grid_column=2)
        self.mid_left = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=1, grid_column=0)
        self.mid_mid = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=1, grid_column=1)
        self.mid_right = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=1, grid_column=2)
        self.btm_left = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=2, grid_column=0)
        self.btm_mid = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=2, grid_column=1)
        self.btm_right = WindowFrame(self.btm_frame, pack_or_grid="grid", grid_row=2, grid_column=2)


        self.top_mid_lbl = CreateLabel(self.top_mid, lbl_text="Important")
        self.top_right_lbl = CreateLabel(self.top_right, lbl_text="Not Important")
        self.mid_left_lbl = CreateLabel(self.mid_left, lbl_text="Time-Sensitive")
        self.btm_left_lbl = CreateLabel(self.btm_left, lbl_text="Not Time-Sensitive")

        """ Fix loc of boxes and labels, already created grid items """

        self.top_left_box = CreateBox(self.mid_mid)
        self.top_right_box = CreateBox(self.mid_right)
        self.btm_left_box = CreateBox(self.btm_mid)
        self.btm_right_box = CreateBox(self.btm_right)

        self.tl = self.top_left_box.listbox
        self.tr = self.top_right_box.listbox
        self.bl = self.btm_left_box.listbox
        self.br = self.btm_right_box.listbox
        self.box_list = [self.tl, self.tr, self.bl, self.br]

    def load_todo(self):
        todo_list_local = get_todos("I_TM.txt")
        for todo in todo_list_local:
            self.top_left_box.listbox.insert(tk.END, f"{todo}")

        todo_list_local2 = get_todos("NI_TM.txt")
        for todo2 in todo_list_local2:
            self.top_right_box.listbox.insert(tk.END, f"{todo2}")

        todo_list_local3 = get_todos("I_NTM.txt")
        for todo3 in todo_list_local3:
            self.btm_left_box.listbox.insert(tk.END, f"{todo3}")

        todo_list_local4 = get_todos("NI_NTM.txt")
        for todo4 in todo_list_local4:
            self.btm_right_box.listbox.insert(tk.END, f"{todo4}")

    def add_todo(self):
        self.todo__add_local = self.entry_box.get()
        if self.todo__add_local != "":
            if self.chk1_int.get() == 1 and self.chk2_int.get() == 1:
                self.top_left_box.listbox.insert(tk.END, self.todo__add_local)
            elif self.chk1_int.get() == 0 and self.chk2_int.get() == 1:
                self.top_right_box.listbox.insert(tk.END, self.todo__add_local)
            elif self.chk1_int.get() == 1 and self.chk2_int.get() == 0:
                self.btm_left_box.listbox.insert(tk.END, self.todo__add_local)
            else:
                self.btm_right_box.listbox.insert(tk.END, self.todo__add_local)
            self.entry_box.delete(0, tk.END)
        else:
            messagebox.showwarning("showwarning", "Please, Enter New Item in Text Box!")

    def edit_todo(self):
        self.todo_edit_local = self.entry_box.get()
        if self.todo_edit_local != "":
            for item in self.box_list:
                if not item.curselection():
                    continue
                else:
                    for item1 in item.curselection():
                        item.delete(item1)
                        item.insert(item1, f"{self.todo_edit_local}")
            self.entry_box.delete(0, tk.END)
        else:
            messagebox.showwarning("showwarning", "Please, Enter Replacement Item in Text Box!")

    def del_todo(self):
        for item in self.box_list:
            if not item.curselection():
                continue
            else:
                for item1 in item.curselection():
                    item.delete(item1)

    def save_todo(self):
        write_todos(list(self.top_left_box.listbox.get(0, tk.END)), "save_files/I_TM.txt")
        write_todos(list(self.top_right_box.listbox.get(0, tk.END)), "save_files/NI_TM.txt")
        write_todos(list(self.btm_left_box.listbox.get(0, tk.END)), "save_files/I_NTM.txt")
        write_todos(list(self.btm_right_box.listbox.get(0, tk.END)), "save_files/NI_NTM.txt")

    def exit_todo(self): #, list_box_obj):
        self.destroy()



"""

window = tk.Tk()
window.config(background="black")

window.title("To Do Application")
window.geometry("600x500")


top_frame = tk.Frame(window)
top_frame.pack(fill=tk.BOTH, expand=tk.YES)

top_frame.columnconfigure(1, weight=1)
top_frame.rowconfigure(1, weight=1)

window_top_text = tk.Label(top_frame, text="Type To Do: ", bg="#50727B", fg="white")
window_top_text.grid(row=0)

window_entry_box = tk.Entry(top_frame)
window_entry_box.grid(row=0, column=1, sticky=tk.NSEW)


list_scroll_frame = tk.Frame(top_frame)
list_scroll_frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW, pady=10)
window_list_box_scroll = tk.Scrollbar(list_scroll_frame)
window_list_box_scroll.pack(side=tk.RIGHT, fill=tk.Y)
window_list_box = tk.Listbox(list_scroll_frame, yscrollcommand=window_list_box_scroll.set)
window_list_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
window_list_box_scroll.config(command=window_list_box.yview)

window_entry_box.bind("<Return>", func=lambda event, list_obj=window_list_box: add_to_do_w_key(event, list_obj))
window_add_button = tk.Button(top_frame, text="Add", command=lambda: add_to_do(window_entry_box, window_list_box))
window_add_button.grid(row=0, column=2, sticky=tk.EW)

side_buttons_frame = tk.Frame(top_frame)
side_buttons_frame.grid(row=1, column=2, sticky=tk.NSEW, pady=5)
window_edit_button = tk.Button(side_buttons_frame, text="Edit",
                               command=lambda: edit_to_do(window_entry_box, window_list_box))
window_edit_button.grid(row=0, sticky=tk.EW)

window_delete_button = tk.Button(side_buttons_frame, text="Delete", command=lambda: delete_to_do(window_list_box))
window_delete_button.grid(row=1, sticky=tk.EW)

window_exit_button = tk.Button(side_buttons_frame, text="Exit", command=lambda: save_do_todo(window, window_list_box))
window_exit_button.grid(row=2, sticky=tk.EW)

load_todos(window_list_box)

"""

def main():
    check_files()
    MainWindow().mainloop()


if __name__ == "__main__":
    main()