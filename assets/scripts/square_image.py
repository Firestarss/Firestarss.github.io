from PIL import Image
import argparse

def add_image_borders(image_path, output_path, color):
    # Open the image
    image = Image.open(image_path)

    # Get the original width and height
    width, height = image.size

    # Determine the maximum dimension
    max_dimension = max(width, height)

    # Calculate the border sizes
    horizontal_border = (max_dimension - width) // 2
    vertical_border = (max_dimension - height) // 2

    # Create a new image with borders
    bordered_image = Image.new(image.mode, (max_dimension, max_dimension), color)
    bordered_image.paste(image, (horizontal_border, vertical_border))

    # Save the modified image
    bordered_image.save(output_path)

if __name__ == "__main__":
    # Example usage
    # input_image_path = input("Path to input file")
    # output_image_path = "output.jpg"
    # add_image_borders(input_image_path, output_image_path)

    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=str, help="Input file path")
    parser.add_argument("-o", "--output", type=str, default=None, help="Output file path. Defaults to input file path")
    parser.add_argument("-c", "--color", type=int, default=(0,0,0), nargs="+", help="Fill color as (R,G,B) tuple")

    args = parser.parse_args()

    if args.output is None: args.output = args.input
    args.color = tuple(args.color)

    add_image_borders(args.input, args.output, args.color)

    print("Done")