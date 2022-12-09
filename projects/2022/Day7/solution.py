import os

file_path = os.path.dirname(os.path.realpath(__file__))

def change_dir(file_path, dir):
    if dir == '/':
        file_path.clear()
        file_path.append('')
    elif dir == '..':
        del file_path[-1]
    else:
        file_path.append(dir)

def update_dir_sizes(sys_data, file_path, sum_file_size):
    sys_data['size'] += sum_file_size

    for sub_path in file_path[1:]:
        if sub_path not in sys_data['subfolders']:
            sys_data['subfolders'][sub_path] = {'size': sum_file_size, 'subfolders': {}}
        else:
            sys_data['subfolders'][sub_path]['size'] += sum_file_size

        sys_data = sys_data['subfolders'][sub_path]

def process_files(sys_data, file_path, metadata_list):
    sum_file_size = sum([int(line.split(' ')[0]) for line in metadata_list if line.split(' ')[0].isdigit()])
    update_dir_sizes(sys_data, file_path, sum_file_size)

def process_commands(input, file_path=[]):
    sys_data = {'size': 0, 'subfolders': {}}
    for command in input:
        if command.startswith('cd'):
            change_dir(file_path, command.split()[1])
        elif command.startswith('ls'):
            process_files(sys_data, file_path, command.strip().split('\n')[1:])

    return sys_data

# Returns an object containing file-system data. This is a nested structure that contains the size of each folder as well as an object containing its sub-folder data.
def read_input_and_transform(filename):
    with open(filename) as f:
        return process_commands(f.read().split('$ '))

def get_folder_sizes(sys_data, list=[]):
    list.append(sys_data['size'])
    [get_folder_sizes(sys_data['subfolders'][subfolder], list) for subfolder in sys_data['subfolders'].keys()]
    return list

def get_sum_folder_size_under_threshold(folder_sizes, threshold=100000):
    return sum(list([x for x in folder_sizes if x <= threshold]))
    
def get_size_of_folder_to_delete(disk_space_used, folder_sizes, total_disk_space=70000000, req_disk_space=30000000):
    space_to_clear = disk_space_used - (total_disk_space - req_disk_space)
    return min(list([x for x in folder_sizes if x >= space_to_clear]))
    
if __name__ == '__main__':
    sys_data = read_input_and_transform(file_path + os.path.sep + 'input.txt')
    folder_sizes = get_folder_sizes(sys_data)

    print(get_sum_folder_size_under_threshold(folder_sizes))
    print(get_size_of_folder_to_delete(sys_data['size'], folder_sizes))