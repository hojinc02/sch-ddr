from util import rgb8_2hsl, hsl2rgb
import numpy as np
from PIL import Image
from gradient import colors

def pixel_to_square(a): 
    if not isinstance(a, np.ndarray): 
        a = np.array(a)
    a = a[np.newaxis, :].repeat(4, axis=0)
    a = a[np.newaxis, :, :].repeat(4, axis=0)
    return a

def save_as_square(a, name): 
    a = hsl2rgb(a)
    a = pixel_to_square(a)
    a = (a * 255.).astype(np.uint8)
    Image.fromarray(a).save(name)


def new_b_d(color_name, bs, bl, ds, dl): 
    rgb = colors[color_name]
    b_delta = np.array([0, bs, bl], dtype=float)
    d_delta = np.array([0, ds, dl], dtype=float)

    hsl = np.array(rgb8_2hsl(rgb), dtype=float)
    b_hsl = hsl + b_delta
    d_hsl = hsl + d_delta
    save_as_square(b_hsl, f'./generated/b_{color_name}.png')
    save_as_square(d_hsl, f'./generated/d_{color_name}.png')
    

new_b_d('turquoise', -30, 14, -10, -40)