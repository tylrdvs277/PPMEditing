# Name:       Tyler Davis
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 6 
# Term:       Spring 2017

import sys

def get_reach_input(arguments):
    if len(arguments) < 2:
        print("Usage: python3 blur.py <image> [<reach>]")
        exit()
    try:
        return int(arguments[2])
    except IndexError:
        return 4
    
def get_file_input(arguments):
    try:
        return open(arguments[1], "r")
    except FileNotFoundError:
        print("Unable to open {0}".format(arguments[1]))
        exit()

def read_file(in_file):
    file_stuff = []
    for line in in_file:
        line = line.strip()
        if line != "":
            file_stuff += line.split(" ")
    return file_stuff

def convert_to_int(nums):
    return [int(num) for num in nums]

def group_by_three(list_1):
    return [list_1[begin : begin + 3] 
            for begin in range(0, len(list_1), 3)] 

def blur_pixel(pixels):
    total = [0 for i in range(len(pixels[0]))]
    for pixel in pixels:
        for idx in range(len(pixel)):
            total[idx] += pixel[idx]
    return [color // len(pixels) for color in total]

def write_to_file(file_content, out_file):
    for list_1 in file_content:
        for element in list_1:
            out_file.write("{0}\n".format(element))

def build_pixs_to_avg(pixels, pix_1d, reach, length, height):
    pix_row = pix_1d // length
    pix_col = pix_1d % length
    return [pixels[row_idx * length + col_idx] 
            for row_idx in range(max(pix_row - reach, 0), 
                min(pix_row + reach, height - 1) + 1)
            for col_idx in range(max(pix_col - reach, 0), 
                min(pix_col + reach, length - 1) + 1)]

def main():
    reach = get_reach_input(sys.argv)
    image_file = get_file_input(sys.argv)
    file_content = read_file(image_file)
    image_file.close()
    (length, height) = (int(file_content[1]), int(file_content[2]))
    pixels = group_by_three(convert_to_int(file_content[4 : ]))
    blurred_pixels = [file_content[ : 4]]
    for idx in range(length * height):
        pixels_to_avg = build_pixs_to_avg(pixels, idx, 
                        reach, length, height)
        blurred_pixels.append(blur_pixel(pixels_to_avg))
    blurred_image = open("blurred.ppm", "w")   
    write_to_file(blurred_pixels, blurred_image)
    blurred_image.close()

if __name__ == "__main__":
    main()
