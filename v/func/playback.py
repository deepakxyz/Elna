import os
# get all the sequences in the directory
def get_sequences():
    sequences = []
    for file in os.listdir():
        if os.path.isfile(file):
            raw, ext = os.path.splitext(file)
            raw = raw.split('.')
            file_name = raw[0] +  ".##" + ext 
            if not file_name in sequences:
                sequences.append(file_name)
        
    return sequences