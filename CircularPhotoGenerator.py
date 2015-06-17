
from __future__ import print_function
__author__ = 'dustinschie'
from PIL import Image, ImageOps, ImageDraw
import os, sys


def center_square_cropped_image(image):
    width, height = img.size
    length = min(width, height)
    size = (length, length)
    return ImageOps.fit(image=image, size=size)


def save_image(image, original_image_name):
    split_name = original_image_name.split(".")
    new_name = split_name[0] + "Circle.png"
    image.save(new_name)


def circle_corners(image):
        w, h = image.size
        rad = min(w, h)
        rad /= 2.0
        rad = round(rad)
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        alpha = Image.new('L', image.size, "White")
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        image.putalpha(alpha)

        outline_draw = ImageDraw.Draw(image)
        outline_draw.ellipse((0, 0, rad * 2, rad * 2), outline="black")

        return image

if __name__ == "__main__":
    for infile in sys.argv[1:]:
        f, e = os.path.splitext(infile)
        orig_name = infile
        img = Image.open(orig_name)
        centered_image = center_square_cropped_image(img)
        circle_image = circle_corners(centered_image)
        save_image(circle_image, f + ".png")


