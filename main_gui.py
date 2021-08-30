# File will be used to build the gui based on diciontary input in a file

import tkinter as tk
import component_loader
import scrollbar
import tag_definitions as td

rt = tk.Tk()
rt.title("Tag Encode/Decoder")
rt.geometry("1000x700")

#initialize scrollbar
root = scrollbar.create_scroll_window(rt)

# load dictionary with tag definitions
tag_dict = td.emv_dict

# give the dictionary to the component loader to build the frame
component_loader.load_components(root, tag_dict)

tk.mainloop()