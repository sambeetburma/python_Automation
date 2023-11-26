with open("file.txt", "r") as f:
    read_content = f.readlines()
    print(read_content)
    for line in read_content:
        print(line, end="")
