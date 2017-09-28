# Name:       Tyler Davis
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 6 
# Term:       Spring 2017

import sys

def valid_args(arguments):
    if len(arguments) < 2:
        print("Usage: python3 decode.py <image>")
        exit()

def get_input_file(arguments):
    try:
        return open(arguments[1], "r")
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

def decode_pixel(pixel, max_color):
    pixel[0] = min((int(pixel[0])) * 10, max_color)
    for idx in range(1, len(pixel)):
        pixel[idx] = pixel[0]
    return pixel

def write_to_file(list_1, out_file):
    for element in list_1:
        out_file.write("{0}\n".format(element))

def main():
    valid_args(sys.argv)
    image_file = get_input_file(sys.argv)
    decoded_image = open("decoded.ppm", "w")
    header = read_file(image_file, 4)
    max_color = int(header[3])
    write_to_file(header[ : 4], decoded_image)
    pixels_to_place = group_by_three(header[4 : ])
    for pixel_counter in range(int(header[1]) * int(header[2])):
        try:
            if len(pixels_to_place[0]) != 3:
                missing = 3 - len(pixels_to_place[0])
                old_pixels = pixels_to_place.pop(0)
                old_pixels += read_file(image_file, missing) 
                pixels_to_place = group_by_three(old_pixels)
        except IndexError:
            pixels_to_place = group_by_three(read_file(image_file, 3))
        write_to_file(decode_pixel(pixels_to_place.pop(0), max_color), 
                      decoded_image)
    image_file.close()
    decoded_image.close()

if __name__ == "__main__":
    main()
