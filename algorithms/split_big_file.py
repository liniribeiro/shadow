


def split_file():

    name = "folder.txt"
    # this loads the first file fully into memory
    with open(f"folder/{name}", 'r', encoding="ISO-8859-1") as f:
        csvfile = f.readlines()

    linesPerFile = 160000
    filename = 1
    # this is better then your former loop, it loops in 1000000 lines a peice,
    # instead of incrementing 1000000 times and only write on the millionth one
    for i in range(0, len(csvfile), linesPerFile):
        with open(f"xanana_{str(filename)}.txt", 'w+', encoding="ISO-8859-1") as f:
            if filename > 1:  # this is the second or later file, we need to write the
                f.write(csvfile[0])  # header again if 2nd.... file
            f.writelines(csvfile[i:i + linesPerFile])
        filename += 1


split_file()