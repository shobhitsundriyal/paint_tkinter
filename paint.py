from tkinter import *

root = Tk()
root.title('paint')
root.geometry('800x800')

def paint(e):
    # e is event that keeps track of mouse
    # Brush parameters
    brush_width = 20
    brush_color = 'green'
    brush_type = BUTT #BUTT(SLASH), ROUND, PROJECTING(DIAMOND)

    #start pos
    x1 = e.x - 1
    y1 = e.y - 1
    
    #Ending position
    x2 = e.x + 1
    y2 = e.y + 1
    canvas.create_line(x1, y1, x2, y2, fill=brush_color, width=brush_width, capstyle=brush_type, smooth=True)



w = 600
h = 400
canvas = Canvas(width=w, height=h, bg='white')
canvas.pack(pady=20)

canvas.bind('<B1-Motion>', paint) # left click mouse

#Brush options
brush_option_frame = Frame(root)
brush_option_frame.pack(pady=20)


root.mainloop()