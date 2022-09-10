# file_name = "r.txt"
# with open(file_name) as file:
#     text = file.read()
#     print(text)
#     new_text = text[::-1]
#     print(new_text)
# with open("new_file.txt", "w") as file:
# file.write(new_text)
file_name = "r.txt"
with open(file_name) as file:
    for i in file:
        print(i)
        out = i[::-1]
        print(out)
        with open("out.txt", "a") as f:
            f.write(out)