import cv2
import numpy as np

# Define board size and square size
board_size = 8  # 8x8 chessboard
square_size = 50  # Size of each square in pixels

# Calculate image size
img_size = board_size * square_size

# Create a blank image
chessboard = np.zeros((img_size, img_size, 3), dtype=np.uint8)

# Draw the squares
for i in range(board_size):
    for j in range(board_size):
        # Check if the square should be white or black
        if (i + j) % 2 == 0:
            color = (255, 255, 255)  # White color
        else:
            color = (0, 0, 0)  # Black color
        
        # Define the top-left and bottom-right corners of the square
        top_left = (j * square_size, i * square_size)
        bottom_right = ((j + 1) * square_size, (i + 1) * square_size)
        
        # Draw the square on the image
        cv2.rectangle(chessboard, top_left, bottom_right, color, -1)

# Display the chessboard
cv2.imshow("Chessboard", chessboard)
cv2.imwrite('result\chess.jpg',chessboard)
cv2.waitKey(0)
cv2.destroyAllWindows()