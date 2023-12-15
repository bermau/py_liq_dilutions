"""Create an image from an IPL code"""


field_1 = "25121245"
field_2 = "98"
field_3 = "TEST second"
field_4 = "31/12/1964 M"
now = "2023/23/15 10:23"
nb_labels= 3

ipl_format_for_Epp_1_5_ml = f"""
<STX><ESC>C<ETX><STX><ESC>P<ETX><STX>E5;F5;<ETX>
<STX>H01;o315,565;b0;f2;h01;w01;c34;d3,{field_1};<ETX>
<STX>H02;o55,565;b1;f2;h01;w01;c31;d3,{field_2};<ETX>
<STX>H04;o315,520;b0;f2;h01;w01;c34;d3,{field_3};<ETX>

<STX>H05;o315,455;b0;f2;h02;w01;c2;d3,{field_4};<ETX>
<STX>H06;o315,415;b0;f2;h01;w01;c30;d3,{now};<ETX>

/* ligne */
<STX>L07;o315,380;f2;l1300;w4<ETX>
# <STX>B10;o125,115;c2;f3;h160;w03;i0;d3," + ";<ETX>

/* afficher ALIQUOT BIO MOL   */
<STX>H14;o315,300;b1;f2;h01;w01;c31;d3,BIOMOL;<ETX>

/* Mini étiquette pour couvercle */
<STX>H16;o315,100;b0;f2;h01;w01;c31;d3,{field_1};<ETX>
<STX>H17;o315,65;b0;f2;h01;w01;c31;d3,{field_3};<ETX>
<STX>R<ETX><STX><ESC>E5<CAN><ETX><STX><RS>{nb_labels}<ETB><ETX>
"""

import re
from PIL import Image, ImageDraw, ImageFont

def generate_image_from_ipl(ipl_code, image_path):
    # Create a new image with white background
    image = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(image)

    # Use a monospaced font for consistent spacing
    font = ImageFont.load_default()

    # Remove comments delimited by /* */
    ipl_code = re.sub(r'/\*.*?\*/', '', ipl_code, flags=re.DOTALL)

    # Remove leading newlines from each command_type
    ipl_code = ipl_code.replace('\n<', '<')

    # Split the IPL code by <ETX> to get individual commands
    commands = ipl_code.split("<ETX>")

    for command in commands:
        # Extract relevant information from the command
        parameters = command.split(";")
        command_type = parameters[0]

        if command_type.startswith("<STX>H"):
            # Handle text commands
            x = int(parameters[1].split(",")[0][1:])
            y = int(parameters[1].split(",")[1])
            text = parameters[-2].split(",")[1]
            if parameters[-2] == 'h01':
                direction = 'ttb'
            else:
                direction = 'ttb'
                print(direction)
            draw.text((x, y), text, fill="black", font=font, directino = direction)

        elif command_type.startswith("<STX>L"):
            # Handle line commands
            x1 = int(parameters[1].split(",")[1][1:])
            y1 = int(parameters[2].split(",")[0][1:])
            length = int(parameters[4][1:])
            draw.line([(x1, y1), (x1 + length, y1)], fill="black", width=4)

    # Save the generated image
    image.save(image_path)

# Example usage
ipl_code = ipl_format_for_Epp_1_5_ml

image_path = "generated_label.png"
generate_image_from_ipl(ipl_code, image_path)


