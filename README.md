# raw_to_bmp
Interpret a raw binary file to a square monochrome bitmap. Usefull for eyeballing a file's entropy.

# Usage
python3 script.py input.dat output.bmp

# Test data
included in this repository is 

* smile.dat - Converts to a 8x8 pixel smiley. Each byte corresponds to a row of 8 pixels.
* random.org.dat - 16k of random data downloaded from random.org
