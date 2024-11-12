from flask import Flask, render_template, request, redirect, url_for, flash
from source.database.db_init import db
from source.models.Property import Property
from source.models.Inquiry import Inquiry
from source.utils.consts import TEMPLATE_DIR, STATIC_DIR, DB_PATH, KEY

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Home route: Shows all listings
@app.route('/')
def home():
    properties = Property.query.all()
    return render_template('home.html', properties=properties)


# Property detail route
@app.route('/property/<int:property_id>')
def property_detail(property_id):
    property = Property.query.get_or_404(property_id)

    property.hit_counter += 1
    db.session.commit()

    return render_template('property.html', property=property)


# Route to increment the view count (hit counter) for the property
@app.route('/property/<int:property_id>/increment', methods=['POST', 'GET'])
def increment_hit_counter(property_id):
    property = Property.query.get_or_404(property_id)
    property.hit_counter += 1
    db.session.commit()
    return redirect(url_for('property_detail', property_id=property_id))


# Signup form route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Save inquiry to the database
        new_inquiry = Inquiry(name=name, email=email, phone=phone, message=message)
        db.session.add(new_inquiry)
        db.session.commit()

        flash('Thank you for signing up! An agent will contact you soon.', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html')
