class Movie():

    def __init__(self,id,title,ranking,description) -> None:
        self.id = id
        self.title = title
        self.ranking = ranking
        self.description = description

    def to_json(self):
        return {
            'id': self.id,
            'title':self.title,
            'ranking':self.ranking,
            'description':self.description
        }