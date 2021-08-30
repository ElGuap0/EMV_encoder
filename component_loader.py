# File used to load the EMV dictionary entries to the gui
import tkinter as tk
import tag_box

def build_len_dict(in_dict):
    # assume ip is a dictionary where each key pair value is the name
    # of a tag and its value is an array holding all of its byte values
    # ie. 'tag_name': [b8, b7, b6 ..... b1]
    # detect the length in bytes of an array
    # assume the array has at least 8 bits and length is a multiple of 8
    # if a dictionary exists as one of the entries then adjust for it

    op = {}
    for tag in in_dict:

        # check if any of the elements in the array are dictionaries that store 2 bit combos
        dict_cnt = 0 # keep track of number of dictionaries encountered
        for val in in_dict[tag]:

            if type(val) == dict:
                dict_cnt += 1

        if dict_cnt != 0:
            # since we know each dictionary contains 2 bits we can adjust like this
            op[tag] = int( ( len(in_dict[tag]) + ((2*dict_cnt)-1) ) /8 ) 
        else:
            # if no bit combos are detected
            op[tag] = int( len(in_dict[tag]) /8 )
    return op

def load_components(root, input_dict):
    # input_dict should be a dictionary of dictionaries where each entry is a tag definition
    # this function will turn each entry into its own encoder/decoder box and pack it into root
    
    tags_len_dict = build_len_dict(input_dict)
    
    for tag in input_dict:
        tag_len = tags_len_dict[tag]
        frame = tk.LabelFrame(root, width=70,height=70, text=tag)
        frame.pack(fill='both', side='top', expand='no')
        tag_decoder = tag_box.Tag_box(frame, tag, tag_len, input_dict)