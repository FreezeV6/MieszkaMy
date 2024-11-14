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


# Signup form route (property_id is optional)
@app.route('/signup', defaults={'property_id': None}, methods=['GET', 'POST'])
@app.route('/signup/<int:property_id>', methods=['GET', 'POST'])
def signup(property_id):
    # Retrieve property_id from form data if available, and convert it to an integer or set to None
    form_property_id = request.form.get('property_id')
    if form_property_id and form_property_id.strip() != "NULL":
        try:
            property_id = int(form_property_id)
        except ValueError:
            property_id = None
    else:
        property_id = None

    print("Server Debug - property_id:", property_id, "Type:", type(property_id))

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Create the Inquiry object, passing property_id as None if not set
        new_inquiry = Inquiry(
            name=name,
            surname=surname,
            email=email,
            phone=phone,
            message=message,
            property_id=property_id  # This will be None if not provided
        )

        db.session.add(new_inquiry)
        db.session.commit()

        flash('Thank you for signing up! An agent will contact you soon.', 'success')
        return redirect(url_for('home'))  # Change to 'confirm' if needed

    return render_template('signup.html', property_id=property_id)


# dodac signup confirm page, jak jest zwrotka 200
@app.route('/signup/confirm')
def confirm():
    return render_template('signup_confirm.html')
