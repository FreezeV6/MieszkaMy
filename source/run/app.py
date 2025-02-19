from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail #Message

from source.database.db_init import db
from source.models.Property import Property
from source.models.Inquiry import Inquiry
from source.utils.consts import TEMPLATE_DIR, STATIC_DIR, DB_PATH, KEY

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
app.secret_key = KEY

app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['MAIL_SERVER'] = 'smtp.mailgun.org'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'postmaster@sandbox4b0e6d03bbf7457a9413546799aa9cd1.mailgun.org'
app.config['MAIL_PASSWORD'] = '4726a6ddadd1d0164b47075c32dedce0-c02fd0ba-e7eb0e92'
app.config['MAIL_DEFAULT_SENDER'] = 'mieszkamy@sandbox4b0e6d03bbf7457a9413546799aa9cd1.mailgun.org '

mail = Mail(app)


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


@app.route('/signup', defaults={'property_id': None}, methods=['GET', 'POST'])
@app.route('/signup/<int:property_id>', methods=['GET', 'POST'])
def signup(property_id):
    form_property_id = request.form.get('property_id')
    if form_property_id:
        try:
            property_id = int(form_property_id)
        except ValueError:
            property_id = None

    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        new_inquiry = Inquiry(
            name=name,
            surname=surname,
            email=email,
            phone=phone,
            message=message,
            property_id=property_id
        )

        db.session.add(new_inquiry)
        db.session.commit()

        # Send email to agent
        # agent_email = "jakismail@dodac.trzeba"
        # email_subject = "New Client Signup"
        # email_body = f"""
        # A new client has signed up:
        # Name: {name} {surname}
        # Email: {email}
        # Phone: {phone}
        # Message: {message}
        # Property: {property_id}
        # """
        #
        # msg = Message(email_subject, recipients=[agent_email])
        # msg.body = email_body
        #
        # try:
        #     mail.send(msg)
        # except Exception as e:
        #     flash('Signup successful, but failed to send email to the agent.', 'error')
        #     print(f"Email error: {e}")

        flash('Thank you for signing up! An agent will contact you soon.', 'success')
        return redirect(url_for('confirm'))

    return render_template('signup.html', property_id=property_id)


@app.route('/signup/confirm')
def confirm():
    return render_template('signup_confirm.html')
