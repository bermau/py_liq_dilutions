from local import my_printer, printer_list
import subprocess
from datetime import datetime

nb_labels = 3

field_1 = "25121245"
field_2= "98"
field_3 = "TEST second"
field_4 = "31/12/1964 M"
sDatPrel = "15/02/2023"
now = datetime.now().strftime("%Y/%m/%d %H:%M")

ipl_format_for_Epp_1_5_ml = f"""
<STX><ESC>C<ETX><STX><ESC>P<ETX><STX>E5;F5;<ETX>
<STX>H01;o315,565;b0;f2;h01;w01;c34;d3,{field_1};<ETX>

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


def print():
    with open("etiq.txt", 'w') as f:
        f.writelines(ipl_format_for_Epp_1_5_ml)

    subprocess.check_output(["copy", ".\etiq.txt", my_printer], shell=True)

if __name__ == '__main__':
    print()