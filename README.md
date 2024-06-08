# Message Hider Stegonography Tool

Small tool which can be used to encrypt an alphabetical message into an image. To encrypt you select a message, offset, rgb component (r, g or b), image and base.   

The tool works by adjusting the rgb component selected of each offset'th pixel such that that pixels rgb component value % base = character. 

The tool does not preserve characters not a-z and does not preserve capitalization.

## Example:
Message: "abcd" -> "1234"
Offset: 15
Base: 31
RGB Component: 0 (red)

Pixel transformation in given image:
- Pixel 0: (100, 100, 100) -> (94, 100, 100) - (94 % 31 = 1)
- Pixel 15: (60, 255, 255) -> (33, 255, 255) - (33 % 31 = 2)
- Pixel 30: (30, 255, 255) -> (3, 255, 255) - (3 % 31 = 3)
- Pixel 45: (2, 255, 255) -> (4, 255, 255) - (4 % 31 =  4)