#file used to encode the emv tag values from checkboxes
import tag_definitions as td
import tag_box
from tkinter import *


def encode_tag(input_panel, tag_name):
    # we assume the input is one of the Tag_decoder_box objects in tag_box.py

    tag_dict = td.emv_dict[tag_name]
    output = ''

    # iterate through the dictionary so we do not neet to find the bit location
    # bc we know it as we go through
    for i in tag_dict: 
        
        #if a dictionary is encountered we know a bit combo is used
        if type(i) == dict:
            #decode the dictionary entry
            #reverse the dictionary to have access to the bit combos
            inv = dict(zip(i.values(), i.keys()))

            #search for the checkbox in the panel, if it is found and the value is true set
            #the corresponding bits in the result
            t = '00'

            for checkbox in input_panel.checkboxes:
                if (checkbox in inv) and (input_panel.checkboxes[checkbox].get() == True):
                    t=inv[checkbox]
            
            # build output
            output+=t
        
        #normal condition
        else:
            #append the value of the box as a string
            output+=str(int(input_panel.checkboxes[i].get()))

    input_panel.input_tag.set(tohex(output))

def tohex(val_in):
    # convert a binary string with zero padding to a hexidecimal value as a string
    # need to convert to hex by one nibble at a time to preserve zero padding.

    o = ''

    for i in range(int(len(val_in)/4)):
        s = val_in[i*4:(i*4)+4]
        o += hex(int(s,2))[2:]

    return o.upper()

if __name__ == '__main__':

    root = Tk()
    
    tag_name = 'tvr' #tag name should match dict name
    master_dict = td.emv_dict
    testbox = tag_box.Tag_box(root, tag_name, master_dict)
    
    root.mainloop()