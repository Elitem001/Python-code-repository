import tkinter as tk
from math import sin, cos, radians, pi

window = tk.Tk()
window.title("Hokejové ihrisko")


canvas_width = 1000
canvas_height = 500


canvas = tk.Canvas(window, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

def olympijske_kruhy():
    x, y = 380, 200
    r = 50
    dx, dy = 120, 60
    canvas.create_oval(x - r, y - r, x + r, y + r,
                   outline='blue', width=15)
    canvas.create_oval(x - r + dx/2, y - r + dy, x + r + dx/2, y + r + dy,
                   outline='yellow', width=15)
    canvas.create_oval(x - r + dx, y - r, x + r + dx, y + r,
                   outline='black', width=15)
    canvas.create_oval(x - r + dx + dx/2, y - r + dy, x + r + dx + dx/2, y + r + dy,
                   outline='limegreen', width=15)
    canvas.create_oval(x - r + 2*dx, y - r, x + r + 2 * dx, y + r,
                   outline='red', width=15)


#funkcie na obly obdlznik
def part_circle (xS, yS, r, alpha, beta, color='black'):
    # xS, yS suradnice stredu kruznice s polomerom r
    # alpha < beta; zaciatok a koniec vykreslenej casti kruhu (0 - 3 hodiny, 90 - 12 hodin)
    
    x_start = int (round (xS + cos(radians(alpha))*r) )
    y_start = int (round (yS - sin(radians(alpha))*r) )
    
    step = 60/(pi*r)
    for theta in range ( int (round(alpha/step)), int (round(beta/step))):
        theta*=step
                         
        x_end = int (round (xS + cos(radians(theta))*r) )
        y_end = int (round (yS - sin(radians(theta))*r) )

        canvas.create_line (x_start, y_start, x_end, y_end, fill=color)

        x_start, y_start = x_end, y_end



def wide_part_circle (xS, yS, r, alpha, beta, width, color='black'):
    for rn in range (r, r+width):
        part_circle (xS, yS, rn, alpha, beta, color)


def rounded_rectangle (lhx, lhy, pdx, pdy, r, width=1, color='black'):
    #lave horne x, y, prave dolne x, y, polomer kruznic pri rohoch
    canvas.create_rectangle (lhx+r, lhy-width, pdx-r,lhy, fill=color)
    wide_part_circle (pdx-r, lhy+r, r, 0, 90, width+1, color)

    canvas.create_rectangle (pdx, lhy+r, pdx+width, pdy-r, fill=color)
    wide_part_circle (pdx-r, pdy-r, r, 270, 360, width+1, color)

    canvas.create_rectangle (lhx+r, pdy, pdx-r, pdy+width, fill=color)
    wide_part_circle (lhx+r, pdy-r, r, 180, 270, width+1, color)

    canvas.create_rectangle (lhx-width, lhy+r, lhx, pdy-r, fill=color)
    wide_part_circle (lhx+r, lhy+r, r, 90, 180, width+1, color)

#spracovanie obrazkov
svk=tk.PhotoImage(file='svk.png')
cze=tk.PhotoImage(file='cze.png')
can=tk.PhotoImage(file='can.png')
usa=tk.PhotoImage(file='usa.png')
fin=tk.PhotoImage(file='fin.png')
swe=tk.PhotoImage(file='swe.png')
ger=tk.PhotoImage(file='ger.png')
sui=tk.PhotoImage(file='sui.png')

timy=['svk', 'cze', 'can', 'usa', 'fin', 'swe', 'ger', 'sui']
loga=[svk, cze, can, usa, fin, swe, ger, sui]
print('Timy: ', timy)

#input timov
tim1=str(input('Vyber si prvy hokejovy tim: '))
left=timy.index(tim1)
logo1=loga[left]

tim2=str(input('Vyber si druhy hokejovy tim: '))
right=timy.index(tim2)
logo2=loga[right]

#vykreslenie loga
canvas.create_image(225, canvas_height//2, image=logo1)
canvas.create_image(canvas_width-225, canvas_height//2, image=logo2)

#brankove ciary
canvas.create_line(100, 45, 100, canvas_height - 45, width=5, fill='red')
canvas.create_line(canvas_width-100, 45, canvas_width-100, canvas_height - 45, width=5, fill='red')

#ciary
canvas.create_line(canvas_width // 2, 40, canvas_width // 2, canvas_height - 40, width=10, fill='red')
canvas.create_line(350, 40, 350, canvas_height - 40, width=10, fill='darkblue')
canvas.create_line(650, 40, 650, canvas_height - 40, width=10, fill='darkblue')

# stredny kruh
canvas.create_oval(canvas_width//2-75, canvas_height//2-75, canvas_width//2+75, canvas_height//2+75, width=3, outline='blue')
wide_part_circle (500, 40, 50, 180, 360, 5, 'red')

# ostatne buly
r=5
lx=375
px=625
hy=125
dy=375
canvas.create_oval(lx-r, hy-r, lx+r, hy+r, fill='red', outline='')
canvas.create_oval(px-r, hy-r, px+r, hy+r, fill='red', outline='')
canvas.create_oval(lx-r, dy-r, lx+r, dy+r, fill='red', outline='')
canvas.create_oval(px-r, dy-r, px+r, dy+r, fill='red', outline='')

# vykreslenie ihriska 
rounded_rectangle(40, 40, canvas_width-40, canvas_height-40, 100, 5)
olympijske_kruhy()

#lava branka
canvas.create_line(80, canvas_height // 2 - 50, 80, canvas_height // 2 + 50, width=10)
canvas.create_line(80, canvas_height // 2 - 50, 100, canvas_height // 2 -50, width=10)
canvas.create_line(80, canvas_height // 2 + 50, 100, canvas_height // 2 + 50, width=10) 

#prava branka
canvas.create_line(canvas_width - 80, canvas_height // 2 - 50, canvas_width - 80, canvas_height // 2 + 50, width=10)
canvas.create_line(canvas_width - 80, canvas_height // 2 - 50, canvas_width - 100, canvas_height // 2 - 50, width=10)
canvas.create_line(canvas_width - 80, canvas_height // 2 + 50, canvas_width - 100, canvas_height // 2 + 50, width=10)

# stredne buly
canvas.create_oval(canvas_width // 2 - 10, canvas_height // 2 - 10, canvas_width // 2 + 10, canvas_height // 2 + 10, fill="white", outline='')
canvas.create_oval(canvas_width // 2 - 8, canvas_height // 2 - 8, canvas_width // 2 + 8, canvas_height // 2 + 8, fill="blue", outline='')

# koniec programu 
window.mainloop()
