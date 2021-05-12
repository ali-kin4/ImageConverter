from PIL import Image
from tkinter import filedialog
import tkinter as tk

root = tk.Tk()
root.withdraw()
files = filedialog.askopenfilenames(title='Choose files')

in_format = 'webp'
out_format = 'gif'

for file in files:
    im = Image.open('{}'.format(file))
    im.info.pop('background', None)
    im.save('{}.{}'.format(file.replace('.{}'.format(out_format), ''), out_format), out_format, save_all=True)