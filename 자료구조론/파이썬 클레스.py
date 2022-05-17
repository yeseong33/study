class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id

best = Student('oh',101)
print(Student('oh',101).name)
print(best.get_name())
print(best.get_id)
print(Student('oh',101).get_id())
print(type(best))
