import tkinter as tk
import math

width = height = 300
unit_size = 100

root = tk.Tk()
canvas = tk.Canvas(root, width=width, height=height)
canvas.pack()

def converges(c):
    z = 0.0
    for i in range(200):
        z = z**2 + c
        if math.sqrt(z.real**2 + z.imag**2) >= 2:
            return False
    return True

def coords_to_complex(x, y):
    return complex(
        (x - width//2) / unit_size,
        (y - height//2) / unit_size
    )

def complex_to_coords(z):
    return (
        (z.real * unit_size) + width//2,
        (z.imag * unit_size) + height//2
    )

for y in range(height):
    for x in range(width):
        if converges(coords_to_complex(x, y)):
            canvas.create_rectangle( (x, y)*2 )

root.mainloop()