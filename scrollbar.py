from tkinter import *
from tkinter import ttk

#root = Tk()
#root.geometry("500x400")

def create_scroll_window(root):

    #create a main frame
    main_frame = Frame(root)
    main_frame.pack(fill = BOTH, expand = 1)

    #create canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill=BOTH, expand=1)

    #add scrollbar to canvs
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    #configure the canvas to have the scrollbar
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    #create another frame inside the canvas
    second_frame = Frame(my_canvas)

    # add that new frame to a window in the canvas
    my_canvas.create_window((0,0), window=second_frame, anchor = "nw")

    return second_frame

if __name__ == "__main__":
    root = Tk()
    root.geometry("500x400")

    sroot = create_scroll_window(root)

    for i in range(50):
        Button(sroot, text=f'Button {i}').grid(row = i, column = 0 , pady = 10, padx=10)

    sroot.mainloop()