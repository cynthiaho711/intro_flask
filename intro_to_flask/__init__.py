from flaskapp import Flask

app = Flask(__name__)
 
app.secret_key = 'development key'
 
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'dorocyn@gmail.com'
app.config["MAIL_PASSWORD"] = 'spring88'

from routes import mail 
mail.init_app(app)

import intro_to_flask.routes
