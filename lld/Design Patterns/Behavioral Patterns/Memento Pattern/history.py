from text_memento import Text_Momento
from typing import List


class History:
    def __init__(self):
        self.__history: List[Text_Momento] = []
        self.__redo: List[Text_Momento] = []

    def save_state(self, tm: Text_Momento):
        self.__history.append(tm)
        self.__redo.clear()

    def undo(self) -> Text_Momento:
        if len(self.__history) <= 1:
            return self.__history[0] if self.__history else Text_Momento("")

        undone = self.__history.pop()
        self.__redo.append(undone)
        return self.__history[-1]

    def redo(self) -> Text_Momento:
        if not self.__redo:
            return self.__history[-1] if self.__history else Text_Momento("")

        restored = self.__redo.pop()
        self.__history.append(restored)
        return restored
