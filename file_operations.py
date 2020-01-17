def import_board(filename):
    try:
        with open(filename, mode='r') as file:
            file_content = file.readlines()
        for i, line in enumerate(file_content):
            row = []
            for char in line:
                if char != "\n":
                    row.append(char)
            file_content[i] = row
        return file_content
    except FileNotFoundError:
        print(f"File '{filename}' not found!")


def export_board(board_state, filename):
    # STEP 1: prepare a string with data to save to the file
    string_to_export = ""
    for line in board_state:
        for character in line:
            string_to_export += f"{character}"
        string_to_export += "\n"
    # STEP 2: write data to file in txt format
    try:
        with open(filename, mode='w') as file:
            file.write(string_to_export)
    except PermissionError:
        print(f"You don't have permission creating file '{filename}'!")
