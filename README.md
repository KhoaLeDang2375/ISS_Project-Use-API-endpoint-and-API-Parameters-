﻿# ISS_Project-Use-API-endpoint-and-API-Parameters-
# ISS Tracker and Notifier

This Python script checks the location of the International Space Station (ISS) and notifies the user via email if the ISS is visible from a specified location.

## Features
- Tracks the ISS's position in real-time using the [open-notify.org API](http://api.open-notify.org/iss-now.json).
- Checks the sunrise and sunset times for your location to ensure it is dark enough to see the ISS.
- Sends an email notification if the ISS is overhead and it's currently dark.
- Runs automatically every 60 seconds.

## Requirements
- Python 3.x
- Internet connection for API requests and sending emails.

## Setup Instructions
1. **Install Dependencies**:
   Make sure you have the following Python libraries installed:
   - `requests`
   - `smtplib` (built-in)
   - `datetime` (built-in)
   - `time` (built-in)

   To install `requests`, use:
   ```bash
   pip install requests
