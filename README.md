# EMV_encoder
Used to encoder and decode EMV or other tags. The EMV_encoder is intended to help encode/decode EMV tags that might be used from time to time to avoid lookup in documents. 
The tag definitions should be added to the tag_definitions.py file which comes which some tags already (TVR, Application Usage Control, Issuer Action Codes), more can be added by adding another dictionary in the master dicitonary.
By running the main.py file the GUI will be launched with an individual encoding box for each of the tags in the dictionary. The encoder can also handle proprietary tags which may use nested 2 bit encoding (ie. as per the TVR).
