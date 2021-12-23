# 20 - Duck Typing


class TextBox:
    def draw(self):
        print("TextBox")


class DropDownList:
    def draw(self):
        print("DropDownList")


class RadioButton:

    def draw(self):
        print("RadioButton")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
txtbox = TextBox()
rdb = RadioButton()


# polymorfism without using subclasses of a main abstract class, there is just needed to have implemented the same mathod.
draw([ddl, txtbox, rdb])
