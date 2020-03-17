from flask import Flask
from sensehat import SenseHat
# sense hat activeren
sense = SenseHat()
# init flask server
app = Flask(_name_)

sense_val = {
	'val' : '#000000',
	'type' : 'hex'
}

@app.route('/')
def index():
	return 'Greetings earthlings lockdown ga nog gelijk vree lang duren!'

@app.route('/pi')
def pi():
	return 'dit is de pi van Arne stop met slechte code te runnen via mij!'

		
