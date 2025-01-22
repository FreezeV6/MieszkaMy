from source.database.db_init import db


class Property(db.Model):
    __tablename__ = 'properties'

    property_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    prop_location = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=True)  # Optional field for more property details
    image = db.Column(db.String(100), nullable=True)
    hit_counter = db.Column(db.Integer, default=0)  # New field to count hits
    property_area = db.Column(db.Numeric(10, 2), default=0.0)
