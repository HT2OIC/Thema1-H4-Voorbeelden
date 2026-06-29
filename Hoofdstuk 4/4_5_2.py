# Rect-object als constante aanmaken
RECHTHOEK = Rect((10, 10), (200, 100))
screen.draw.filled_rect(RECHTHOEK, "blue")

# Rect-object niet afzonderlijk aanmaken
screen.draw.filled_rect(Rect((10, 10), (200, 100)), "blue")

# 4 getallen afzonderlijk als argumenten
vierkant = Rect(10, 10, 100, 100)