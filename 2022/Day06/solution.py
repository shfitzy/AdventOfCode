import os

file_path = os.path.dirname(os.path.realpath(__file__))

# Nothing crazy with this one, just returns the input
def read_input_and_transform(filename):
    with open(filename) as f:
        return f.read()

# Returns the ending index (1-indexed) of the first sub-section of n-characters that are all unique, where n is the size of the marker
# This method works by creating a set of n-characters and checking the size of the set - if it is equal to the marker size, we immediately return that index
def calc_start_of_packet(input, marker_size=4):
    return(next((i + marker_size) for i in range(len(input) - (marker_size - 1)) if (len(set(input[i:i+marker_size])) == marker_size)))

if __name__ == '__main__':
    input = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    
    print(calc_start_of_packet(input))
    print(calc_start_of_packet(input, 14))