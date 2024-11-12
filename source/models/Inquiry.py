from source.database.db_init import db


class Inquiry(db.Model):
    __tablename__ = 'inquiries'

    inquiry_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)
    property_id = db.Column(db.Integer, db.ForeignKey('properties.property_id'), nullable=True)
