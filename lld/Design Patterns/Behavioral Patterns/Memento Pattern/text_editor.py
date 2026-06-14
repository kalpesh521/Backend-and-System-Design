from text_memento import Text_Momento

class TextEditor:
    def __init__(self):
        self.__text = ""

    def write(self , new_text):
        self.__text += new_text

    def get_text(self):
        return self.__text

    def save(self) -> Text_Momento:
        return Text_Momento(self.__text)

    def restore(self, tm: Text_Momento):
        self.__text = tm.get_saved_text()