image: list[str] = []

with open("input.txt") as f:
    algo = f.readline().replace("\n", "")
    f.readline()
    r = f.readlines()
    for row in r:
        image.append(row.replace("\n", ""))

reference: dict[str, str] = {bin(n)[2:].zfill(9).replace("1", "#").replace("0", "."): algo[n] for n in range(2**9)}

new_image = ["." * (len(image[0]) + 8)] * 4
new_image += ["...." + row + "...." for row in image]
new_image += ["." * (len(image[0]) + 8)] * 4
image = new_image

for k in range(2):
    new_c = reference["." * 9] if k % 2 else reference[reference["." * 9] * 9]
    new_image = [new_c * (len(image[0]) + 2)]
    new_image += [new_c + row + new_c for row in image]
    new_image += [new_c * (len(image[0]) + 2)]
    image = new_image.copy()

    new_c = reference[reference["." * 9] * 9] if k % 2 else reference["." * 9]
    new_image = [new_c * (len(image[0]))]
    new_image += [new_c + row[1:-1] + new_c for row in image[1:-1]]
    new_image += [new_c * (len(image[0]))]

    for i in range(1, len(image) - 1):
        for j in range(1, len(image[0]) - 1):
            key = image[i-1][j-1:j+2] + image[i][j-1:j+2] + image[i+1][j-1:j+2]
            new_image[i] = new_image[i][:j] + reference[key] + new_image[i][j+1:]
    image = new_image

print(sum(sum(1 if c == "#" else 0 for c in row) for row in image))
