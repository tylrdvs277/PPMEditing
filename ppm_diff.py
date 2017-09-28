# Name:        Tyler Davis
# Course:      CPE 101
# Instructor:  Nupur Garg
# Assignment:  ppm diff
# Term:        Spring 2017

from sys import argv

def main():
    files = open_files()
    file_content = []
    for file_1 in files:
        file_content.append(group_by_three(read_file(file_1)))
    diffs = diff_pixels(file_content)
    if diffs != 0:
        print("Images differ ({0} pixels)".format(diffs))

def open_files(args = argv[1 : ]):
    if len(args) != 2:
        print("Usage: python3 ppm_diff.py <image1> <image2>")
        exit()
    try:
        return (open(args[0], "r"), 
                open(args[1], "r"))
    except:
        print("File Cannot Be Opened")
        exit()

def read_file(file_1):
    content = []
    for line in file_1:
        line = line.strip()
        if line != "":
            content += line.split(" ")
    return content[4 : ]

def group_by_three(list_1):
    grouped = []
    for idx in range(0, len(list_1), 3):
        grouped.append(list_1[idx : idx + 3])
    return grouped

def diff_pixels(files):
    diffs = 0
    for (pixel_1, pixel_2) in zip(files[0], files[1]):
        if not list_epsilon_equal(pixel_1, pixel_2):
            diffs += 1
    return diffs

def list_epsilon_equal(list_1, list_2, epsilon = 1):
    for (x, y) in zip(list_1, list_2):
        if not (abs(int(x) - int(y)) <= epsilon):
            return False
    return True

if __name__ == "__main__":
    main()
