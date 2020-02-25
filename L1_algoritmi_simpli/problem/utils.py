import os

def getAbsolutePath(filePath: str, relativePath: str) -> str:
    fileDir = os.path.dirname(__file__)
    absolutePath = os.path.join(fileDir, relativePath)
    return absolutePath
