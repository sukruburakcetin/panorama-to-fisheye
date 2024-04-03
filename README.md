# panorama-to-fisheye

Import Libraries:

cv2: OpenCV library for image processing.
numpy as np: NumPy library for numerical operations.
panoramic_to_fisheye Function:

This function takes a panoramic image as input and returns the fisheye version of the image.
It extracts the height and width of the input panoramic image.
Calculates the dimensions of the fisheye image based on the minimum of its height and width, setting it to have a width of twice its height to maintain a 2:1 aspect ratio.
Initializes an empty array to store the fisheye image.
Defines the center and radius of the circular fisheye region.
Creates a binary mask to identify the circular region of interest in the fisheye image.
Loops through each pixel in the fisheye image, checks if it falls within the circular mask, and calculates the corresponding polar coordinates.
Maps the polar coordinates to the equirectangular coordinates of the panoramic image.
Handles edge cases where the mapped coordinates may exceed the bounds of the panoramic image.
Copies the pixel value from the panoramic image to the fisheye image.
Example Usage:

Loads a panoramic image using OpenCV's imread function.
Calls the panoramic_to_fisheye function to convert the panoramic image to a fisheye image.
Saves the fisheye image using OpenCV's imwrite function.
Prints a success message after saving the fisheye image.