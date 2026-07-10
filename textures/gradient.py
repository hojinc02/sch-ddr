import numpy as np
from PIL import Image
import math
from util import floats_to_str, rgb8_2hsl, rgb2hsl, hsl2rgb, sigmoid_smooth

colors = {
    'red': (255, 0, 0),
    'blue': (1, 1, 255),
    'yellow': (250, 250, 0),
    'pink': (228, 0, 243),
    'turquoise': (13, 198, 160),
    'green': (1, 255, 1),
    'orange': (255, 153, 0),
    'sky_blue': (44, 215, 255)
}

bright_colors = {
    'red': (253, 121, 121),
    'blue': (134, 134, 253),
    'yellow': (255, 255, 108),
    'pink': (242, 162, 255),
    'turquoise': (149, 248, 219),
    'green': (166, 254, 166),
    'orange': (255, 188, 89),
    'sky_blue': (157, 225, 255)
}

if __name__=="__main__": 

    for name, rgb in colors.items(): 
        colors[name] = rgb8_2hsl(rgb)
    for name, rgb in bright_colors.items(): 
        bright_colors[name] = rgb8_2hsl(rgb)
        
    m = 32
    sm = 14
    sig_s, sig_e = -1, 4

    for band_color in colors.keys(): 

        start_color = bright_colors[band_color]
        end_color = colors[band_color]

        hue_vals = np.full((sm, 1), end_color[0])
        sat_vals = sigmoid_smooth(start_color[1], end_color[1], sm, sig_s, sig_e)[:, np.newaxis]
        lig_vals = sigmoid_smooth(start_color[2], end_color[2], sm, sig_s, sig_e)[:, np.newaxis]

        band = np.array(hsl2rgb(colors[band_color]))
        band = band[np.newaxis, :].repeat(m, axis=0)

        start_band = np.hstack((hue_vals, sat_vals, lig_vals))
        for i in range(start_band.shape[0]): 
            band[i,:] = hsl2rgb(start_band[i,:])
        
        band *= 255.
        band = band.astype(np.uint8)
        band = band[:, np.newaxis, :].repeat(8, axis=1)
        band = np.concatenate((band, np.flip(band, axis=0)), axis=0)

        img = Image.fromarray(band)
        img.save(f'./generated/band_{band_color}.png')