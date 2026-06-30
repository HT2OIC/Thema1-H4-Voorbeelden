clock.schedule_unique(mario_reset, 0.5)

def mario_reset():
    """Reset Mario naar de lopende afbeelding."""
    mario.image = "mario_lopen"