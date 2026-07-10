import numpy as np
from PIL import Image, ImageDraw

START_PIXEL = np.array((64, 0, 64), dtype=np.uint8)

if __name__=="__main__": 
    img = Image.open('Tap Note parts (mipmaps).png').convert('RGB')
    arr = np.array(img)
    flood_indices = np.argwhere(np.all(arr == START_PIXEL, axis=2))
    
    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)
    
    fill = (0, 0, 0, 0)
    
    for m in range(len(flood_indices)): 
        
        i, j = int(flood_indices[m][0]), int(flood_indices[m][1]) + 1
        draw.point((j - 1, i), fill)
        ImageDraw.floodfill(img, (j, i), fill)
    
    img.save('new.png')