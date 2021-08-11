from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from matplotlib import pyplot as plt

root = Tk()
root.title("Graph Maker")
def drawgraph():
    x1 = []
    y1 = []
    try:
        for item in List_x:
            x1.append(float(item.get()))
        for item in List_y:
            y1.append(float(item.get()))
        plt.plot(x1, y1, "-o")
        for x, y in zip(x1, y1):
            plt.text(x, y, '({}, {})'.format(x, y))
            
        if(len(msgbox_E_Graph_name.get()) > 1):
            g_name = str(msgbox_E_Graph_name.get())
        else:
            g_name = "Graph!"

        if (len(msgbox_E_x_name.get())>1):
            x_name = str(msgbox_E_x_name.get())
        else :
            x_name = "X-Axis"
        if (len(msgbox_E_y_name.get())>1):
            y_name = str(msgbox_E_y_name.get())
        else:
            y_name = "Y-Axis"

        plt.title(g_name, fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
        plt.xlabel(x_name, fontdict={'fontname': 'Comic Sans MS'})
        plt.ylabel(y_name, fontdict={'fontname': 'Comic Sans MS'})
        plt.show()
    except:
        messagebox.showerror("Error", "Please provide valid input")
        msgbox_B['state'] = NORMAL
        nw.destroy()

def New_Window(number):
    global nw
    nw = Toplevel()
    nw.title("Graph Maker")
    nw.geometry("1200x900")
    msgbox_B["state"] = DISABLED
    main_frame = Frame(nw)
    main_frame.pack(fill=BOTH, expand=1)
    my_canva = Canvas(main_frame)
    my_canva.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canva.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canva.configure(yscrollcommand=my_scrollbar.set)
    my_canva.bind('<Configure>', lambda e: my_canva.configure(scrollregion=my_canva.bbox("all")))
    global second_frame
    second_frame = Frame(my_canva)
    my_canva.create_window((0, 0), window=second_frame, anchor="nw")
    global i
    global List_x
    global List_y
    List_x = []
    List_y = []
    try:

        for i in range(int(number)):

            msgbox_xL = Label(second_frame, text=f"Enter The X{i+1} Co-ordinate:")
            msgbox_yL = Label(second_frame, text=f"Enter The Y{i+1} Co-ordinate:")

            msgbox_xL.grid(row=i, column=0, columnspan=2)
            msgbox_yL.grid(row=i, column=10, columnspan=2)

            msgbox_xE = Entry(second_frame, width=20, border=5)
            msgbox_xE.grid(row=i, column=2)
            List_x.append(msgbox_xE)

            msgbox_yE = Entry(second_frame, width=20, border=5)
            msgbox_yE.grid(row=i, column=15)
            List_y.append(msgbox_yE)
        global nw_Enter
        nw_Enter = Button(second_frame, text="Plot a Graph!",padx=5, pady=5, command=drawgraph)
        nw_Enter.grid(row=i+2, column=2, columnspan=3, padx=10, pady=10)
        nw_retry = Button(second_frame, text="Retry",padx=5, pady=5, command=retry)
        nw_retry.grid(row=i+2, column=4, columnspan=3, padx=10, pady=10)

    except:
        messagebox.showerror("Error", "Please provide valid input")
        msgbox_B['state'] = NORMAL
        nw.destroy()


def retry():
    nw.destroy()
    msgbox_B['state'] = NORMAL


msgbox_L = Label(root, text="Enter How Many Pairs Of Co-Ordinates You Want To Display :")
msgbox_L.grid(row=0, column=0)

msgbox_E = Entry(root, width=50, borderwidth=5)
msgbox_E.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

msgbox_L_Graph_name = Label(root, text="Enter The Graph Name")
msgbox_L_Graph_name.grid(row=1, column=0)

msgbox_E_Graph_name = Entry(root, width=50, borderwidth=5)
msgbox_E_Graph_name.grid(row=1, column=2, columnspan=3, padx=10, pady=10)

msgbox_L_x_name = Label(root, text="Enter The X-Axis Name")
msgbox_L_x_name.grid(row=2, column=0)

msgbox_E_x_name = Entry(root, width=50, borderwidth=5)
msgbox_E_x_name.grid(row=2, column=2, columnspan=3, padx=10, pady=10)

msgbox_L_y_name = Label(root, text="Enter The Y-Axis Name")
msgbox_L_y_name.grid(row=3, column=0)

msgbox_E_y_name = Entry(root, width=50, borderwidth=5)
msgbox_E_y_name.grid(row=3, column=2, columnspan=3, padx=10, pady=10)

msgbox_B = Button(root, text="Enter", padx=5, pady=5,command=lambda: New_Window(msgbox_E.get()))
msgbox_B.grid(row=4, column=2)


root.mainloop()
