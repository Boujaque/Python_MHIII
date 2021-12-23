# 21- Extending Built-in Types
# inheriting from built in types
class Text(str):   # inherit from the strig class
    def duplicate(self):   # adding duplicating method
        return self + self


text = Text("Python")
print(text.lower())

print(text.duplicate())

# extending the List class


class TrackableList(list):
    def append(self, object):
        print("Append Called for ", object)
        super().append(object)


list = TrackableList()
list.append("1")
list.append("2")
list.append("Heiruku")
print(list)
