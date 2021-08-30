from tag_definitions import *

def decode(tag_vals, tag_name, tag_len):
    # function to decode the bits set in the tag
    i = 0 #used to iterate the tag value
    j = 0 #used to iterate the dictionary
    bits_set = [] #result
    tag_dict = emv_dict[tag_name]

    # convert the input into binary
    tag_vals_bin = bin(int('0x'+ tag_vals, 16))
    tag_vals_bin = tag_vals_bin[2:] #get rid of 0b

    tag_len_bits = 8*tag_len

    # this is done to pad the left side with zeros if the transformations above removed a leading zero
    if (len(tag_vals_bin)) != ( tag_len_bits ): 
        tag_vals_bin = tag_vals_bin.zfill(tag_len_bits) 

    val_bin = tag_vals_bin.zfill(tag_len_bits)

    len_tag = len(val_bin)

    #iterate through the dict with respect to the tag value
    while( i < len_tag ):

        # if we reach an index of the tag dictionary that contains another dictionary,
        # we need to encode and increase i by 2
        if type( tag_dict[j] ) == dict:

            bits_set.append( tag_dict[j][ val_bin[i] + val_bin[i+1] ] )
            i += 2
            
        #otherise decode the single bit and add 1  
        else:
            if ( int(val_bin[i]) ):
                bits_set.append( tag_dict[j] )
            i+=1
            
        j += 1
    
    return bits_set

if __name__ == "__main__":

    auc = 'C080'
    
    bits_set =  decode(auc,'auc_dict') 

    for i in bits_set: print(i)