from app import db


class User(db.model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    name = db.Column(db.String)

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name

    def __repr__(self):
        return '<App User %r>' % self.username


class Posts(db.model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('users', foreign_keys=idUser)

    def __init__(self, content, userId):
        self.content = content
        self.idUser = userId

    def __repr__(self):
        return '<App Post %r>' % self.id


class Follow():
    __tablename__ = 'follow'

    id = db.Column(db.Integer, primary_key=True)
    followerId = db.Column(db.Integer, db.ForeignKey('users.id'))
    followedId = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower = db.relationship('users', foreign_keys=followerId)
    followed = db.relationship('users', foreign_keys=followedId)
