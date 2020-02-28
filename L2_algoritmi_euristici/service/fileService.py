

class FileService:

    def __init__(self):
        pass

    def readTextFromFile(self, filePath) -> str:
        text = ""
        with open(filePath, "r") as fileDescriptor:
            for line in fileDescriptor:
                text += line
        return text
    
    def saveTextToFile(self, filePath, text):
        with open(filePath, "w") as fileDescriptor:
            fileDescriptor.write(text)
