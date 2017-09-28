# Name:       Tyler Davis
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 6 
# Term:       Spring 2017

import sys
import math

def valid_args(arguments):
    if len(arguments) < 5:
        print("Usage: python3 fade.py <image> <row>"
              " <column> <radius>")
        exit()

def get_inputs(arguments):
    try:
        return (open(arguments[1], "r"), int(arguments[2]), 
                int(arguments[3]), int(arguments[4]))
    except FileNotFoundError:
        print("Unable to open {0}".format(arguments[1]))
        exit()

def read_file(in_file, list_len):
    file_content = []
    while len(file_content) < list_len:
        line = in_file.readline().strip()
        if line != "":
            file_content += line.split(" ")
    return file_content

def group_by_three(list_1):
    return [list_1[begin : begin + 3] 
            for begin in range(0, len(list_1), 3)] 

def compute_fade_factor(radius, distance):
    return max(((radius - distance) / radius), 0.20)

def get_distance(x1, x2, y1, y2):
    return math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

def fade_pixel(pixel, fade_factor):
    return [int(int(color) * fade_factor) for color in pixel]

def write_to_file(list_1, out_file):
    for element in list_1:
        out_file.write("{0}\n".format(element))

def main():
    valid_args(sys.argv)
    (image_file, row, column, radius) = get_inputs(sys.argv)
    faded_image = open("faded.ppm", "w")
    header = read_file(image_file, 4)
    write_to_file(header[ : 4], faded_image)
    image_width = int(header[1])
    pixels_to_place = group_by_three(header[4 : ])
    for pixel_counter in range(image_width * int(header[2])):
        try:
            if len(pixels_to_place[0]) != 3:
                missing = 3 - len(pixels_to_place[0])
                old_pixels = pixels_to_place.pop(0)
                old_pixels += read_file(image_file, missing) 
                pixels_to_place = group_by_three(old_pixels)
        except IndexError:
            pixels_to_place = group_by_three(read_file(image_file,3))
        pixel_row = pixel_counter // image_width
        pixel_col = pixel_counter % image_width
        distance = get_distance(pixel_row, row, pixel_col, column)
        fade_factor = compute_fade_factor(radius, distance)
        write_to_file(fade_pixel(pixels_to_place.pop(0), fade_factor), 
                      faded_image)
    image_file.close()
    faded_image.close()

if __name__ == "__main__":
    main()
