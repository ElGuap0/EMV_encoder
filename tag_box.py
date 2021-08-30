import sys
sys.path.append(".")
import tag_decoder
import tag_encoder
from tkinter import *
import tag_definitions as td

# Create and load checkboxes and an entry field into a tkinter frame
# Only a BooleanVar which is associated with the Box is saved in a dictionary 
# ...which is accessed by the name of checkbox created by the tag value
# ...this is because only BoolVar is needed to change the box value
class Tag_box:

    def __init__(self, root, tag_name, tag_len, master_dict):
        # build a box that contains:
        # - all bit descriptions of the tags with a checkbox
        # - an encode and decode button
        # - an entry box to write the value to decode
        self.tag_len = tag_len
        tag_dict= master_dict[tag_name] # experimental, added this now
        self.checkboxes = {}  # holds the BoolVar associated to intended flag.
        self.tag_name = tag_name
        self.input_tag = StringVar()
        self.myEntry = Entry(root, text='test val', textvariable=self.input_tag)
        self.tag_label = Label(root,  text = '-- '+tag_name.upper()+' --')
        self.tag_label.grid(row = 0, column = 0)
        self.myEntry.grid(row = 0, column = 1)

        # display the checkboxes in a grid format
        u,v = 0,0 # these variables are used to control when the row and column are incremented
        for i in tag_dict:

            # logic to decode bit combinations stored as a dictionary
            # if a dictionary is detected
            if type( i ) == dict:
                
                for e in i:
                    # create a BoolVar
                    chkvar = BooleanVar()

                    Checkbutton(root, text=i[e], var=chkvar).grid(row = 2+u , column = v)
                    #Checkbutton(root, text=i, var=chkvar).grid(row = 2+u , column = v)
                    self.checkboxes[ i[e] ] = chkvar
                    if (v+1) % 4 == 0:
                        v = 0
                        u += 1
                    else:
                        v += 1

            # normal condition - ie. no bit combos detected
            else:
            
                # create a BoolVar
                chkvar = BooleanVar()

                # create checkbutton, but don't need to save it because we access it with chkvar
                Checkbutton(root, text=i, var=chkvar).grid(row = 2+u , column = v)
                #print('row: ', 1+u , 'col: ', v)

                # save the chkvar/BoolVar associated to the name of the flag, ie'a', so that we can access it in the dictionary
                self.checkboxes[i] = chkvar

                # we print one nibble per row
                if (v+1) % 4 == 0:
                    v = 0
                    u += 1
                else:
                    v += 1

        def decode_entry():
            # clear all checkboxes
            for i in self.checkboxes:
                self.checkboxes[i].set(False)

            #get the value of the tag from the entry box and decode it
            val = self.input_tag.get()
            result = tag_decoder.decode(val, self.tag_name, self.tag_len)

            #set the bits for the relevant checkboxes
            for r in result:
                self.checkboxes[r].set(True)

        def encode_entry():
            tag_encoder.encode_tag(self, self.tag_name)

        self.myButton = Button(root, text='decode', command=decode_entry)
        self.encode_button = Button(root, text='encode', command=encode_entry)
        self.myButton.grid(row = 0, column = 2)
        self.encode_button.grid(row = 0, column = 3)
        self.myEntry.insert(0, '00'*self.tag_len )

if __name__ == '__main__':

    root = Tk()
    tag_name = 'cvr' #tag name should match dict name
    master_dict = td.emv_dict
    testbox = Tag_box(root, tag_name, master_dict)
    root.mainloop()