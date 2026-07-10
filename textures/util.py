from hsluv import hsluv_to_rgb, rgb_to_hsluv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def floats_to_str(l): 
    l = l if isinstance(l, tuple) else tuple(l)
    return '(' + ', '.join([f"{c:.3f}" for c in l]) + ')'

def rgb2hsl(rgb): 
    if isinstance(rgb, np.ndarray): 
        rgb = tuple(rgb)
    return rgb_to_hsluv(rgb)

def rgb8_2hsl(rgb): 
    if not isinstance(rgb, tuple): 
        rgb = tuple(rgb)
    r, g, b = rgb
    r, g, b = r / 255., g / 255., b / 255.
    return rgb_to_hsluv((r, g, b))
    
def hsl2rgb(hsl): 
    if isinstance(hsl, np.ndarray): 
        hsl = tuple(hsl)
    return hsluv_to_rgb(hsl)

def sigmoid_smooth(start, end, n, sig_s=-2, sig_e=2):
    x = np.linspace(sig_s, sig_e, n)
    s = 1 / (1 + np.exp(-x))  
    s = (s - s.min()) / (s.max() - s.min()) 
    return start + (end - start) * s

if __name__=="__main__": 
    update_lightness(1)
    update_lightness(2)