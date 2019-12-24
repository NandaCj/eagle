newline = "\n"

def re_write_file(file, data):
    """
    data should be list of data
    """
    with open(file, 'w+') as f:
        f.write(data)

def retrieve_data_line_by_line(file):
    with open(file, 'r') as f:
        yield f.readline()
