from .. import db


class Carpool(db.Model):
    """ Carpool Model for storing user related details """
    __tablename__ = "carpool"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # TODO: how to remove the  could not assemble any primary key columns for mapped table 'carpool
    driver_id = db.Column(db.String(255), db.ForeignKey('user.id'))
    when = db.Column(db.Date, nullable=False)  # DD/MM/YY
    start = db.Column(db.String(255), nullable=False)  # default=current location
    destination = db.Column(db.String(100), nullable=False)
    hour = db.Column(db.DateTime, nullable=False)
    number_of_sits = db.Column(db.Integer, nullable=False)
    animal = db.Column(db.Boolean)
    road6 = db.Column(db.Boolean)
    comments = db.Column(db.String(255), nullable=False)

    def __str__(self):
        return f"drive number {self.id}, from {self.start}"


