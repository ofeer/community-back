from .. import db, flask_bcrypt


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user"
    id = db.Column(db.String(100), primary_key=True, unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    password_hash = db.Column(db.String(100))
    ride = db.relationship('Carpool', backref='my_ride')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User '{}'>".format(self.username)
