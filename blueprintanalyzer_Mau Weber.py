import cv2
import numpy as np

def open_image(path):
    """Opens an image from the given file path."""
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Could not load the image from: {path}")
    return img

def display_window(title, img_data):
    """Displays the given image data in a window."""
    cv2.imshow(title, img_data)

def grayscale_conversion(img_data):
    """Converts the input image to a single-channel grayscale image."""
    return cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)

def perform_edge_detection(grayscale_img):
    """Uses the Canny algorithm to detect edges in the image."""
    thresholds = (50, 150)  # Lower and upper thresholds for Canny
    return cv2.Canny(grayscale_img, thresholds[0], thresholds[1])

def extract_contours(original, edges):
    """Identifies contours from edge data and draws them over the original image."""
    contours_found, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    annotated_img = original.copy()
    cv2.drawContours(annotated_img, contours_found, -1, (0, 255, 0), 2)
    return contours_found, annotated_img

def measure_areas(contours_found):
    """Measures and prints the area for each contour."""
    all_areas = [cv2.contourArea(c) for c in contours_found]
    for idx, area in enumerate(all_areas, start=1):
        print(f"Shape {idx}: Area = {area:.2f}")
    return all_areas

def export_image(file_path, img_data):
    """Saves the processed image to the provided file path."""
    cv2.imwrite(file_path, img_data)

def run_pipeline():
    """Orchestrates the image processing sequence."""
    source_path = input("Enter the file path of the input image: ")
    result_path = "final_result.png"

    try:
        # 1:Load and show the image
        img = open_image(source_path)
        display_window("Loaded Image", img)

        # 2:Convert to grayscale
        gray_img = grayscale_conversion(img)
        display_window("Grayscale View", gray_img)

        # 3:Detect edges
        edges_detected = perform_edge_detection(gray_img)
        display_window("Detected Edges", edges_detected)

        # 4:Extract contours and draw on the image
        found_contours, img_with_shapes = extract_contours(img, edges_detected)
        display_window("Contours Overlay", img_with_shapes)

        # 5:Compute and report areas of the contours
        measure_areas(found_contours)

        # 6:Save the resulting image
        export_image(result_path, img_with_shapes)
        print(f"Processed image saved to: {result_path}")

        # 7:Wait for user input and close all image windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as err:
        print(f"An error occurred during processing: {err}")

if __name__ == "__main__":
    run_pipeline()
