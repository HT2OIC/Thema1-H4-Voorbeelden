def draw():
    teken_gaten(75)
    teken_gaten(225)
    teken_gaten(375)
    teken_gaten(525)
    teken_gaten(675)

def teken_gaten(x_positie):
    screen.draw.filled_circle((x_positie, 450), 50, "black")
