from Content import Content

class User:
    def __init__(self, id->Long):
        this.id = id
        this.contentList = []
        this.recommendedList = []

    def addContent(self, content->Content):
        this.contentList.append(content)

    def getContentList(self):
        return this.contentList
