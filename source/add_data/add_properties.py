from source.database.db_init import db
from source.models.Property import Property


def add_properties():
    # Create tables and add sample data when the app starts
    if not Property.query.first():
        initial_properties = [
            Property(title='Modern Family Home', prop_location='New York', price='500000',
                     description='A spacious family home in the heart of New York.'),
            Property(title='Luxury Condo', prop_location='San Francisco', price='850000',
                     description='A beautiful condo with stunning views of the city.'),
            Property(title='Cozy Cottage', prop_location='Austin', price='300000',
                     description='A charming cottage with modern amenities.'),
            Property(title='Beachfront Villa', prop_location='Miami', price='1200000',
                     description='A luxurious villa with a private beach in Miami.'),
            Property(title='Mountain Retreat', prop_location='Denver', price='750000',
                     description='A cozy retreat with beautiful mountain views in Denver.')
        ]
        db.session.bulk_save_objects(initial_properties)
        db.session.commit()
