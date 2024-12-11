import sdl2
import sdl2.ext
from sdl2 import rect
import time

# Initialize SDL2
sdl2.ext.init()
window = sdl2.ext.Window("Multiple Car Animation", size=(800, 600))
window.show()
renderer = sdl2.ext.Renderer(window)

# Define car properties
cars = [
    {"x": 50, "y": 450, "width": 100, "height": 50, "speed": 5, "color": (255, 0, 0)},
    {"x": 200, "y": 400, "width": 80, "height": 40, "speed": 3, "color": (0, 255, 0)},
    {"x": 400, "y": 500, "width": 120, "height": 60, "speed": 7, "color": (0, 0, 255)},
]

# Screen dimensions
screen_width, screen_height = 800, 600

# Main loop
running = True
clear_rect = rect.SDL_Rect(0, screen_height - 150, screen_width, 150)  # Area to clear (road)
while running:
    # Handle events
    for event in sdl2.ext.get_events():
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

    # Update car positions
    for car in cars:
        car["x"] += car["speed"]
        if car["x"] > screen_width:
            car["x"] = -car["width"]  # Reset off-screen car

    # Clear the road area
    renderer.set_draw_color(sdl2.ext.Color(50, 50, 50))  # Dark gray road
    renderer.clear(clear_rect)

    # Draw each car
    for car in cars:
        # Draw car body (use renderer.fill for efficiency)
        renderer.fill((car["x"], car["y"], car["width"], car["height"]), car["color"])
        # Draw car tires (use built-in circle drawing)
        renderer.draw_circle(car["x"] + 20, car["y"] + car["height"] - 0, 10, (0, 0, 0))
        renderer.draw_circle(car["x"] + car["width"] - 20, car["y"] + car["height"] - 0, 10, (0, 0, 0))

    # Present the screen
    renderer.present()

# Cleanup
sdl2.ext.quit()