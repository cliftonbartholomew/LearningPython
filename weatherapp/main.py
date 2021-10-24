# weather API libraries
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# import the smtplib module. It should be included in Python by default
import smtplib

# email object packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Setup an Open Weather App object with the supplied API key (you need to subscribe for free to get one)
owm = OWM('32c2b13d5652d5d38c6819010ec025b2')
manager = owm.weather_manager()

# Search for current weather in Durban South Africa
observation = manager.weather_at_place('Durban ,ZA')
w = observation.weather

cloudStatus = w.detailed_status
tempObject = w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
currentTemp = tempObject['temp']


# set up the SMTP server
server = smtplib.SMTP(host='smtp.gmail.com', port=587)
server.ehlo()
server.starttls()
server.login("cliftonbartholomew@gmail.com", "Barcli13")


#create the message
message = """Dear Me,

Temperature is :""" + str(currentTemp) + """\n
Cloud status is : """ + str(cloudStatus) + """\n

Yours Truly,
Other Me"""


msg = MIMEMultipart() #create an email message object

# setup the parameters of the message
msg['From']= "cliftonbartholomew@gmail.com"
msg['To']="cliftonbartholomew@gmail.com"
msg['Subject']="Weather Update From Me"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# send the message via the server set up earlier.
server.send_message(msg)
    
del msg
