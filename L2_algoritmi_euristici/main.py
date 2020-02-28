
from ui.gui import Gui
from service.problemService import ProblemService
from service.fileService import FileService

fileService = FileService()
problemService = ProblemService()

app = Gui(problemService, fileService)
app.run()

