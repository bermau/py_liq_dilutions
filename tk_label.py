import subprocess
from datetime import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from local import my_printer, printer_list

# Ce programme imprime de petites étiquettes pour des tubes de type Eppendorf 1.5 ml
# L'utilisateur dispose de 4 champs.
# L'utilisateur peut décider d'imprimer la date d'impression ou un cinquième champ.

# Fonction pour imprimer les étiquettes
def print_labels():
    field_1 = entry_field_1.get()
    field_2 = entry_field_2.get()
    field_3 = entry_field_3.get()
    field_4 = entry_field_4.get()
    nb_labels = int(entry_nb_labels.get())  # Récupère le nombre d'étiquettes

    if add_date_var.get():
        now = datetime.now().strftime("%Y/%m/%d %H:%M")
    else:
        now = alt_field_for_date.get()


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

    with open("etiq.txt", 'w') as f:
        f.writelines(ipl_format_for_Epp_1_5_ml)

    try:
        subprocess.check_output(["copy", ".\etiq.txt", selected_printer.get()], shell=True)
        messagebox.showinfo("Impression réussie", "Les étiquettes ont été imprimées avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur d'impression", f"Une erreur est survenue lors de l'impression : {str(e)}")

# Fonction pour activer ou désactiver le champ field_5 en fonction de la case à cocher
def toggle_field_5():
    if add_date_var.get():
        alt_field_for_date.grid_remove()  # Masquer le champ field_5
    else:
        alt_field_for_date.grid(row=6, column=1)  # Afficher le champ field_5
        alt_field_for_date.configure(state ='normal')

# Création de la fenêtre principale
root = tk.Tk()
# root.geometry("600x400")
root.title("Générateur d'étiquettes")


# Sélection de l'imprimante
printer_frame = ttk.Frame(root)
printer_frame.grid(row= 0, column=0, rowspan=2, columnspan=2)

label_printer = ttk.Label(printer_frame, text="Sélectionnez l'imprimante :")
label_printer.grid(row = 0, column = 0, pady = 30, sticky='W')

# printer_list = ["Imprimante1", "Imprimante2", "Imprimante3"]  # Remplacez par vos imprimantes réelles
selected_printer = tk.StringVar(value=printer_list[0])
printer_menu = ttk.Combobox(printer_frame, textvariable=selected_printer, values=printer_list)
printer_menu.grid(row = 0, column = 1, sticky='W')

# Champs à remplir
entry_frame = ttk.Frame(root)
entry_frame.grid(pady=20, padx= 50)

label_fields = ttk.Label(entry_frame, text="Remplissez les champs :")
label_fields.grid(row=1, column=0, rowspan=3)

entry_field_1 = ttk.Entry(entry_frame, width=11)
entry_field_1.insert(0, "25121245")
entry_field_1.grid(row=1, column=1, sticky='W')

entry_field_2 = ttk.Entry(entry_frame, width=2)  # Champ 2 réduit à 2 caractères
entry_field_2.insert(0, "98")
entry_field_2.grid(row=1, column=2, sticky='W')

entry_field_3 = ttk.Entry(entry_frame, width=24)
entry_field_3.insert(0, "TEST second")
entry_field_3.grid(row=2, column=1 )

entry_field_4 = ttk.Entry(entry_frame, width=20)
entry_field_4.insert(0, "31/12/1964 M")
entry_field_4.grid(row=3, column=1, sticky='W' )

# Option pour ajouter la date du jour
add_date_var = tk.BooleanVar(value = True)
add_date_checkbox = ttk.Checkbutton(entry_frame, text="Ajouter la date du jour", variable=add_date_var,
                                    command=toggle_field_5)
add_date_checkbox.grid(row=5, column=1)

# Champ pour spécifier le champ field_5 (initialement grisé)
label_field_5 = ttk.Label(entry_frame, text="Champ libre :")
label_field_5.grid(row=6, column=0)

alt_field_for_date = ttk.Entry(entry_frame, width=20,
                               state="disabled"
                               )
alt_field_for_date.grid(row=6, column=1)

# Champ pour spécifier le nombre d'étiquettes à imprimer
last_frame = ttk.Frame(root)
last_frame.grid(pady=20)

label_nb_labels = ttk.Label(last_frame, text="Nombre d'étiquettes à imprimer :")
label_nb_labels.grid(row= 0, column= 0)

entry_nb_labels = ttk.Entry(last_frame, width=5)
entry_nb_labels.insert(0, "3")  # Valeur par défaut
entry_nb_labels.grid(row= 0, column= 1, sticky='W')

# Bouton d'impression
bottom_frame = ttk.Frame(root)
bottom_frame.grid(pady=20)
print_button = ttk.Button(bottom_frame, text="Imprimer", command=print_labels)
print_button.grid(row= 1, column = 1)

root.mainloop()

input("")