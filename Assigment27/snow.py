
import cv2
import numpy as np
from PIL import Image

# Load your background image (replace 'your_image.jpg' with your image file)
img = Image.open('nature.jpg')
img = img.convert("RGB")
img = np.array(img)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# Parameters for snow effect
snowflakes = 200  # Number of snowflakes
snowflake_size = 2  # Size of each snowflake
snow_speed = 2  # Speed of falling snow
frames = 500  # Number of frames for GIF
snow_positions = np.random.randint(0, high=min(img.shape[:2]), size=(snowflakes, 2))

# List to store frames for the GIF
gif_frames = []

for _ in range(frames):
    # Copy the original image
    frame = img.copy()

    # Draw snowflakes
    for pos in snow_positions:
        cv2.circle(frame, (pos[1], pos[0]), snowflake_size, (255, 255, 255), -1)
        pos[0] += snow_speed
        if pos[0] > img.shape[0]:  # Reset if off-screen
            pos[0] = 0
            pos[1] = np.random.randint(0, img.shape[1])

    # Convert frame to RGB and add to gif_frames
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    gif_frames.append(Image.fromarray(frame_rgb))

# Save frames as a GIF
gif_frames[0].save("output/snowfall.gif", save_all=True, append_images=gif_frames[1:], duration=100, loop=0)