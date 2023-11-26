with open("file.txt", "r") as f:
    content_of_file = f.read()
    print("existing content", content_of_file)

with open("file.txt", "w") as f:
    f.write("I m learning API als   o")

with open("file.txt", "a+") as f:
    f.writelines("""\nI am learning selenium as well\nthen i will switch job\nwith great pkg""")
    content_of_file = f.read()
    print("Changes made to file", content_of_file)

