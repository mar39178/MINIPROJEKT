# !/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import tkinter.ttk as ttk
import platform
# from matplotlib import pyplot as plt

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Goniometrické funkce"

    def __init__(self):
        super().__init__(className=self.name)
        ## Basic "all-n-all" setup
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.geometry("1300x700")
        self.resizable(width=tk.FALSE, height=tk.FALSE)
        if platform.system() == "Windows":
            self.iconbitmap("images/icon.ico")

        ## Label Frame setup + Label + Separator
        self.headerFrame = tk.LabelFrame(self, borderwidth = 0, highlightthickness = 0)
        self.headerFrame.pack(side=tk.TOP)
        self.headerLabel = tk.Label(self.headerFrame, text="Goniometrické funkce", font=("Arial", 24))
        self.headerLabel.pack()
        ttk.Separator(self, orient='horizontal').pack(fill=tk.X, padx=2)

        ## Content Frame setup + Options Frame setup + Graph Frame setup
        self.contentFrame = tk.Frame(self, width=1300, height=700)
        self.contentFrame.pack(side=tk.TOP, pady=5)
        self.optionsFrame = tk.LabelFrame(self.contentFrame, text="Výběr", width=700, height=700)
        self.optionsFrame.pack(side=tk.LEFT, padx=5, pady=5)
        self.optionsFrame.pack_propagate(False)
        self.graphFrame = tk.LabelFrame(self.contentFrame, text="Graf", width=600, height=700)
        self.graphFrame.pack(side=tk.RIGHT, padx=5, pady=5)
        self.graphFrame.pack_propagate(False)

        ## Options Frame - display options
        self.displayFrame = tk.Frame(self.optionsFrame)
        self.displayFrame.pack(fill=tk.X)
        self.displayOptVar = tk.StringVar(value="program")
        self.displayOpt1 = tk.Radiobutton(self.displayFrame, text="V Programu", font=(None, 12), variable=self.displayOptVar, value="program")
        self.displayOpt1.pack(side=tk.LEFT, padx=20)
        self.displayOpt2 = tk.Radiobutton(self.displayFrame, text="Samostatně", font=(None, 12), variable=self.displayOptVar, value="standalone")
        self.displayOpt2.pack(side=tk.LEFT, padx=20)
        self.displaySelectBtn = tk.Button(self.displayFrame, text="Vybrat Soubor")
        self.displaySelectBtn.pack(side=tk.RIGHT, padx=20)

        ## Options Frame - graph selections
        self.selectionFrame = tk.Frame(self.optionsFrame)
        self.selectionFrame.pack(pady=50)
        self.selectionFrame.place(relx=.5, rely=.5, anchor=tk.CENTER)

        # Graph selections left side
        self.labelA = tk.Label(self.selectionFrame, text="Hodnota A:")
        self.labelA.grid(row=0, column=0, padx=10, pady=5)
        self.entryA = tk.Entry(self.selectionFrame)
        self.entryA.grid(row=0, column=1, padx=10, pady=5)
        self.labelB = tk.Label(self.selectionFrame, text="Hodnota B:")
        self.labelB.grid(row=1, column=0, padx=10, pady=5)
        self.entryB = tk.Entry(self.selectionFrame)
        self.entryB.grid(row=1, column=1, padx=10, pady=5)
        self.labelC = tk.Label(self.selectionFrame, text="Hodnota C:")
        self.labelC.grid(row=2, column=0, padx=10, pady=5)
        self.entryC = tk.Entry(self.selectionFrame)
        self.entryC.grid(row=2, column=1, padx=10, pady=5)
        self.labelD = tk.Label(self.selectionFrame, text="Hodnota D:")
        self.labelD.grid(row=3, column=0, padx=10, pady=5)
        self.entryD = tk.Entry(self.selectionFrame)
        self.entryD.grid(row=3, column=1, padx=10, pady=5)
        self.labelTypeCBox = tk.Label(self.selectionFrame, text="Typ grafu:")
        self.labelTypeCBox.grid(row=4, column=0, padx=10, pady=5)
        self.typeCBox = ttk.Combobox(self.selectionFrame, values=("sin", "cos", "tg", "cotg"))
        self.typeCBox.grid(row=4, column=1, padx=10, pady=5)

        # Graph selections right side
        self.labelXAxis = tk.Label(self.selectionFrame, text="Osa X:")
        self.labelXAxis.grid(row=0, column=2, padx=10, pady=5)
        self.entryXAxis = tk.Entry(self.selectionFrame)
        self.entryXAxis.grid(row=0, column=3, padx=10, pady=5)
        self.labelYAxis = tk.Label(self.selectionFrame, text="Osa Y:")
        self.labelYAxis.grid(row=1, column=2, padx=10, pady=5)
        self.entryYAxis = tk.Entry(self.selectionFrame)
        self.entryYAxis.grid(row=1, column=3, padx=10, pady=5)
        self.labelName = tk.Label(self.selectionFrame, text="Název:")
        self.labelName.grid(row=2, column=2, padx=10, pady=5)
        self.entryName = tk.Entry(self.selectionFrame)
        self.entryName.grid(row=2, column=3, padx=10, pady=5)
        self.labelLineWidth = tk.Label(self.selectionFrame, text="Tloušťka čar:")
        self.labelLineWidth.grid(row=3, column=2, padx=10, pady=5)
        self.entryLineWidth = tk.Entry(self.selectionFrame)
        self.entryLineWidth.grid(row=3, column=3, padx=10, pady=5)
        self.labelGrid = tk.Label(self.selectionFrame, text="Mřížka:")
        self.labelGrid.grid(row=4, column=2, padx=10, pady=5)
        self.gridChBox = tk.Checkbutton(self.selectionFrame)
        self.gridChBox.grid(row=4, column=3, padx=10, pady=5)

        ## Options Frame - action group
        self.actionFrame = tk.Frame(self.optionsFrame)
        self.actionFrame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)
        self.drawBtn = tk.Button(self.actionFrame, text="Vykreslit", font=(None, 13))
        self.drawBtn.grid(row=0, column=1, pady=10, sticky=tk.NSEW)
        self.equasionLabel = tk.Label(self.actionFrame, text="Funkce:")
        self.equasionLabel.grid(row=1, column=0, padx=10)
        self.equasionDisplay = tk.Text(self.actionFrame, state='disabled', width=30, height=1) # při zapisování se bude muset přepsat na state="normal"
        self.equasionDisplay.grid(row=1, column=1)

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()