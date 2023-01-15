class User():

    def __init__(self, id, name, age, joined,genders) -> None:
        self.id = id,
        self.name = name
        self.age = age
        self.joined = joined
        self.genders = genders


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'joined': self.joined,
        }
