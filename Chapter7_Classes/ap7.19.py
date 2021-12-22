
# 19 - Polymorfism


from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


class RadioButton(UIControl):

    def draw(self):
        print("RadioButton")


def draw(control):
    control.draw()


ddl = DropDownList()
# print(isinstance(ddl, UIControl))
draw(ddl)
txtbox = TextBox()
draw(txtbox)

# making iterable


def draw(controls):
    for control in controls:
        control.draw()


draw([ddl, txtbox])
