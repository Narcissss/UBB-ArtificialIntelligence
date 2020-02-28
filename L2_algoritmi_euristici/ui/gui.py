from tkinter import Tk, Label, Button, Text
from tkinter import filedialog as FileDialog
from tkinter import INSERT, DISABLED, END, NORMAL
from tkinter.scrolledtext import ScrolledText

from domain.problem import Problem, ProblemResult

class Gui:

    def __init__(self, problemService, fileService):
        self._window = Tk()
        self._solveBtn = None
        self._problemText = None
        self._resultText = None
        self._problemService = problemService
        self._fileService = fileService
        self._initUIComponents()

    def run(self):
        self._window.mainloop()

    def _initUIComponents(self):
        self._window.title("AI")
        self._window.geometry("800x600")
        Label(self._window, text = "L2 - Algoritmi euristigi - Greedy", font = ("Helvetica", 16)).grid(row = 0, column = 0, columnspan = 2)
        
        self._problemText = ScrolledText(self._window, width = 60, height = 15)
        self._problemText.grid(row = 1, column = 0, rowspan = 2)
        
        Button(self._window, text = "Load file", command = self._loadFromFile).grid(row = 1, column = 1)
        Button(self._window, text = "Save to file", command = self._saveToFile).grid(row = 2, column = 1)
        
        self._solveBtn = Button(self._window, text = "Solve", font = ('Helvetica', 14), command = self._solveProblem)
        self._solveBtn.grid(row = 3, column = 0, pady = 20)
        
        self._resultText = Text(self._window, width = 60, height = 8)
        self._resultText.grid(row = 4, column = 0)

    def _loadFromFile(self):
        fileName = FileDialog.askopenfilename(initialdir = "./", title = "Select file", filetypes = (("text files", "*.txt"), ("input files", "*.in"), ("text files", "*.txt")))
        if fileName:
            problemData = self._fileService.readTextFromFile(fileName)
            self._problemText.delete(1.0, END)
            self._problemText.insert(END, problemData)
    
    def _saveToFile(self):
        fileName = FileDialog.asksaveasfilename(initialdir = "./", title = "Select file", filetypes = (("text files", "*.txt"), ("all files", "*.*")))
        if fileName:
            text = self._problemText.get(1.0, END)
            self._fileService.saveTextToFile(fileName, text)

    def _solveProblem(self):
        text = self._problemText.get(1.0, END)
        if len(text) > 1:
            problem = Problem(text)
            result = self._problemService.findShothestPath_Greedy(problem)
            self._resultText.config(state = NORMAL)
            self._resultText.delete(1.0, END)
            self._resultText.insert(INSERT, str(result))
            self._resultText.config(state = DISABLED)

