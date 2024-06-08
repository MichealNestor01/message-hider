# Message Hider Stegonography Tool

Small tool which can be used to encrypt an alphabetical message into an image. To encrypt you select a message, offset, rgb component (r, g or b), image and base.   

This tool was made to create a ctf challenge for the Leeds Computing Society CTF. 

The tool works by adjusting the rgb component selected of each offset'th pixel such that that pixels rgb component value % base = character. 

The tool does not preserve characters not a-z and does not preserve capitalization.

## Example:
Message: "abcd" -> "0123"  
Offset: 15  
Base: 31  
RGB Component: 0 (red)  
  
Pixel transformation in given image:
- Pixel 0: (100, 100, 100) -> (93, 100, 100) - (93 % 31 = 0)
- Pixel 14: (60, 255, 255) -> (32, 255, 255) - (32 % 31 = 1)
- Pixel 29: (30, 255, 255) -> (2, 255, 255) - (2 % 31 = 2)
- Pixel 44: (2, 255, 255) -> (3, 255, 255) - (3 % 31 =  3)