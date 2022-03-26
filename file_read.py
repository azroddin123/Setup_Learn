import io


# python code read arabic text from files
with open("arabic_data_word") as file:
    lines = [line.rstrip() for line in file]

print(lines)

dist_arabic_chars = set(lines)
