def convert_file_encode_to_utf8(fileName):

    with open(fileName, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = list()
    for line in lines:
        print(line)
        new_lines.append(line)

    with open(fileName.replace('.log', '.txt'), 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


if __name__ == '__main__':
    fileName = 'log_files/run_pal_mode.log'
    convert_file_encode_to_utf8(fileName)
