total_file_size = 0

directories = []
files = {}

dir_sizes = {}

dir_stack = []

curr_dir = ""

TOTAL_SPACE = 70000000
REQ_EMPTY = 30000000

with open("input.txt") as f:
    r = f.readlines()

    for row in r[1:]:
        a = list(row.split())

        if a[0] == "$":
            if a[1] == "cd":
                if a[2] == "/":
                    curr_dir = ""
                    dir_stack = [""]
                elif a[2] == "..":
                    dir_stack.pop()
                    curr_dir = "" if len(dir_stack) == 0 else dir_stack[-1]
                else:
                    new_dir = curr_dir + "/" + a[2]
                    if new_dir in directories:
                        curr_dir = new_dir
                        dir_stack.append(curr_dir)

        else:
            if a[0] == "dir":
                directories.append(curr_dir + "/" + a[1])

            else:
                filename = curr_dir + "/" + a[1]
                files[filename] = int(a[0])

for file_name, file_size in files.items():
    total_file_size += file_size

threshold = total_file_size - TOTAL_SPACE + REQ_EMPTY

for directory in directories:
    dir_files = [
        filesize for filename, filesize in files.items() if filename.startswith(directory + "/")
    ]

    dir_sizes[directory] = sum(dir_files)

filtered_dir_sizes = [dir_size for dir_size in dir_sizes.values() if dir_size >= threshold]

print(min(filtered_dir_sizes))
