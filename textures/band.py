import numpy as np
from PIL import Image

arr = np.asarray(Image.open('down_roll_head_active.png'))

H, W = arr.shape[0], arr.shape[1]
# H, W, (r,g,b,a)

colors = []
for ro in range(H): 
    cnt = 9
    for co in range(W): 
        r,g,b,a = arr[ro,co,0], arr[ro,co,1], arr[ro,co,2], arr[ro,co,3]
        if max(r,g,b) - min(r,g,b) < 10: 
            continue
        cnt -= 1
        if cnt == 0: 
            colors.append(arr[ro,co,:3].tolist())
            break

indices = np.round(np.linspace(0, len(colors) - 1, 32)).astype(int)
sampled = [colors[i] for i in indices]

print(sampled)

color_band = np.array(sampled, dtype=np.uint8)
color_band = np.concatenate(
    [color_band, np.full_like(color_band, 255, shape=(len(sampled), 1))], axis=1)
color_band = color_band[:, np.newaxis, :].repeat(8, axis=1)

img = Image.fromarray(color_band)
img.save('_roll_head_color_band.png')