# Scorpion

This program takes a list of image file paths as input and displays their format, mode, size, and metadata (EXIF and IPTC data). It uses the pyexiv2 library to extract and display EXIF and IPTC information.

----

## Requirements

- Python3
- Some dependencies :
  ``pip install -r requirements.txt``

----

## Usage

``python3 scorpion.py file1 [file2 ...]``

**Arguments:**

- files: List of image files to parse for metadata.

----

## Tips and Notes

- The Image Metadata Viewer reads from the file system, so make sure the images you want to inspect exist in the provided path.

----

## Contribute
Feel free to submit pull requests or issues if you find any mistakes or have suggestions for improvements.

----

**Note: Ensure that you follow ethical hacking guidelines. Do not use the knowledge gained here for malicious intentions. Always seek permission before attempting to exploit vulnerabilities in any system.**
