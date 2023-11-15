import os

def read_lines(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]
    
def read_file(filepath, filename='input.txt', trim=True, split=False, split_str=' '):
    with open(filepath + os.path.sep + filename) as f:
        data = f.readlines()
        
        if(trim):
            data = [line.strip() for line in data]
        if(split):
            data = [line.split(split_str) for line in data]
            
        return data
     
def get_int_array(filepath, filename='input.txt'):
    data = read_file(filepath)
    return list(map(lambda i: int(i), data))
        

def read(filename):
    with open(filename) as f:
        return f.read()
