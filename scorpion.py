from PIL import Image
import argparse
import os
import pyexiv2

def display_metadata(files):
    """
    This function will display the format, mode, size, EXIF data,
    and IPTC data (if present) for each image file in the list.

    Parameters: files (list): A list of file paths to the image files.
    """
    for file in files:
        if not os.path.isfile(file):
            print(f"File not found: {file}")
            continue

        try:
            image = Image.open(file)
        except IOError:
            print(f"Could not read file: {file}")
            continue

        print(f"\nMetadata for file: {file}")
        print(f"Format: {image.format}")
        print(f"Mode: {image.mode}")
        print(f"Size: {image.size}")

        metadata = pyexiv2.Image(file)
        exif_data = metadata.read_exif()
        if exif_data:
            for key, value in exif_data.items():
                print(f"{key}: {value}")
        else:
            print("No EXIF data found.")

        iptc_data = metadata.read_iptc()
        if iptc_data:
            print("\nIPTC Data:")
            for key, value in iptc_data.items():
                print(f"  {key}: {value}")


def main():
    """
    Main function to handle command-line arguments and display image metadata.
    """
    parser = argparse.ArgumentParser(description="A Scorpion program to display image metadata.")
    parser.add_argument("files", nargs='+', help="The image files to parse for metadata.")
    args = parser.parse_args()

    display_metadata(args.files)

if __name__ == "__main__":
    main()
