from local import my_printer
import subprocess
from datetime import datetime

sNbreEtq = 1

sNomPrenom = "TOTO Léon"
sId1 = "25121245"
sId2 = "98"
sDatNaissSex = "31/12/1964 M"
sDatPrel = "15/02/2023"
now = datetime.now().strftime("%Y/%m/%d %H:%M")

# <STX>H03;o55,565;b1;f2;h01;w01;c34;d3," + [sIdIndex]+ ";<ETX>
# /*<STX>H02;o180,565;b0;f2;h01;w01;c34;d3,{sId2};<ETX> */

msg_mispl = f"""
<STX><ESC>C<ETX><STX><ESC>P<ETX><STX>E5;F5;<ETX>
<STX>H01;o315,565;b0;f2;h01;w01;c34;d3,{sId1};<ETX>

<STX>H04;o315,520;b0;f2;h01;w01;c34;d3,{sNomPrenom};<ETX>

<STX>H05;o315,455;b0;f2;h02;w01;c2;d3,{sDatNaissSex};<ETX>
<STX>H06;o315,415;b0;f2;h01;w01;c30;d3,{now};<ETX>

/* ligne */
<STX>L07;o315,380;f2;l1300;w4<ETX>
# <STX>B10;o125,115;c2;f3;h160;w03;i0;d3," + ";<ETX>

/* afficher ALIQUOT BIO MOL   */
<STX>H14;o315,300;b1;f2;h01;w01;c31;d3,BIOMOL;<ETX>

/* Mini étiquette pour couvercle */
<STX>H16;o315,100;b0;f2;h01;w01;c31;d3,{sId1};<ETX>
<STX>H17;o315,65;b0;f2;h01;w01;c31;d3,{sNomPrenom};<ETX>
<STX>R<ETX><STX><ESC>E5<CAN><ETX><STX><RS>{sNbreEtq}<ETB><ETX>
"""

with open("etiq.txt", 'w') as f:
    f.writelines(msg_mispl)
# copy &1 my_printer
# my_printer = "totu"

script = subprocess.check_output(["copy", ".\etiq.txt", my_printer], shell=True)
