# 9 - Making Custom Containers (custom data structures - example)


class TagCloud:
    def __init__(self):
        self.__tags = {}  # Lesson 10: refactor rename with F2;
        # __tags means private but not 100%

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):    # define the getter
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):  # define the setter
        self.__tags[tag.lower()] = count

    def __len__(self):     # define len check method
        return len(self.__tags)

    def __iter__(self):        # define an iterator
        return iter(self.__tags)


# Operations suported by the custom container
# cloud = TagCloud()  # creat an new object
# len(cloud)  # check how many articles we have
# cloud["python"]  # how many articles with tag python
# cloud["python"] = 10  # set the numbers of articles to 10
# for tag in cloud:  # iterate
#     print(tag)
# Creating object
cloud = TagCloud()
# adding tag
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud.add("java")
cloud.add("java")
cloud.add("Typescript")
# print(cloud.__tags)
# reading a tag with []
# this implementation will throw error if we don't have the requested tag, and also we cannot set a value far the tag
print(cloud["python"])

cloud["python"] = 10
print(cloud["python"])

print(len(cloud))

for tag in cloud:
    print(tag)
# 10- Making private member with "__x"
# print(cloud.tags["Python"]) # generate error becasue Python isn not dict memeber
# print(cloud.__tags["Python"])
# will show : {'_TagCloud__tags': {'python': 10, 'java': 2, 'typescript': 1}}
print(cloud.__dict__)
# : will return {'python': 10, 'java': 2, 'typescript': 1}
print(cloud._TagCloud__tags)
