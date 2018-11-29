import os
from PIL import Image
import matplotlib.pyplot as plt
img = Image.open(os.path.join('Monopoly.jpeg'))
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['figure.dpi'] = 300 


plt.imshow(img)
plt.axis('off')
