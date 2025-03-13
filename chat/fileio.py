def read_key_file(file_path):
    with open(file_path, 'r') as file:
        key_content = file.read()
    return key_content