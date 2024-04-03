import cv2
import numpy as np


def panoramic_to_fisheye(panoramic_image):
    # Extract the height and width of the panoramic image
    panoramic_height, panoramic_width = panoramic_image.shape[:2]

    # Calculate the dimensions of the fisheye image
    fisheye_height = min(panoramic_height, panoramic_width)  # Set height to be minimum of width and height
    fisheye_width = fisheye_height * 2  # Set width to be twice the height to maintain 2:1 aspect ratio

    # Initialize an empty array to store the fisheye image
    fisheye_image = np.zeros((fisheye_height, fisheye_width, 3), dtype=np.uint8)

    # Calculate fisheye parameters
    center_x = fisheye_width // 2  # Calculate the x-coordinate of the center
    center_y = fisheye_height // 2  # Calculate the y-coordinate of the center
    radius = min(center_x, center_y)  # Calculate the radius of the circular fisheye region

    # Create a binary mask to identify the circular region of interest in the fisheye image
    mask = np.zeros((fisheye_height, fisheye_width), dtype=np.uint8)
    cv2.circle(mask, (center_x, center_y), radius, 255, -1)  # Draw a filled circle on the mask

    # Convert panoramic image to fisheye
    for y in range(fisheye_height):
        for x in range(fisheye_width):
            if mask[y, x] == 255:  # Check if the pixel falls within the circular region of interest
                # Calculate polar coordinates
                theta = np.arctan2(y - center_y, x - center_x)  # Angle relative to the center
                rho = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)  # Distance from the center

                # Map polar coordinates to equirectangular coordinates of the panoramic image
                panoramic_x = int((theta / np.pi + 1) * (panoramic_width / 2))  # Map angle to width
                panoramic_y = int((rho / radius) * panoramic_height)  # Map distance to height

                # Handle edge cases where the mapped coordinates may exceed the bounds of the panoramic image
                if panoramic_x >= panoramic_width:
                    panoramic_x = panoramic_width - 1
                if panoramic_y >= panoramic_height:
                    panoramic_y = panoramic_height - 1

                # Copy pixel value from panoramic image to fisheye image
                fisheye_image[y, x] = panoramic_image[panoramic_y, panoramic_x]

    return fisheye_image


# Example usage
panoramic_img = cv2.imread('1656703801680.png')  # Load the panoramic image
fisheye_img = panoramic_to_fisheye(panoramic_img)  # Convert the panoramic image to fisheye

# Save fisheye image
cv2.imwrite('fisheye_image.jpg', fisheye_img)  # Save the fisheye image
print("Fisheye image saved successfully!")  # Print a success message
