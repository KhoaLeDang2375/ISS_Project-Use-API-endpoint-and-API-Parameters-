import requests
import smtplib
from datetime import datetime
import time

my_email="23520740@gm.uit.edu.vn"
password= "xhbkzupycxdwgrxm"

def Send_Mail(message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ledangkhoa11a1@gmail.com",
                            
                            msg="Subject:Subject: Look Up\n\n"+message)
MY_LAT = 11.314580 # Your latitude
MY_LONG = 106.094254 # Your longitude
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def ISS_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (iss_latitude <= MY_LAT+5 and iss_latitude>=MY_LONG-5) and (iss_longitude <= MY_LONG+5 and iss_longitude>=MY_LONG-5):
        return True
    return False
#Your position is within +5 or -5 degrees of the ISS position.


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
while True:
    time.sleep(60)
    time_now = datetime.now()

    if sunrise <= time_now.hour or sunset >= time_now.hour and ISS_overhead()==True:
        Send_Mail("Now! You can see ISS!")
        print("Chay ma thanh cong co the nhin thay!")
    else:
        print("Chay ma thanh cong khong the nhin thay!") 
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



