try:
    file = open('resource.txt', 'r')
    print(file.read())
    file.close()

except FileNotFoundError as e:
    print("file not found", e)
else:
    print("File reading completed successfully")
finally:
    print("close the file")
