def convert_file_encode_to_utf8(fileName):
    with open(fileName, 'r') as f:
        lines = f.readlines()
    for line in lines:
        print(line.strip())


if __name__ == '__main__':
    fileName = 'log_files/run_pal_mode.log'
    convert_file_encode_to_utf8(fileName)
