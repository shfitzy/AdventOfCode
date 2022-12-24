
def read_lines(filename):
     with open(filename) as f:
        return [line.strip() for line in f.readlines()]

def read(filename):
    with open(filename) as f:
        return f.read()
