I built this because I kept hearing about "security headers" and had no idea what they actually meant, so instead of just reading about it, I built a tool that checks them.

## What it actually does
You give it a website, and it checks whether that site is using 6 common security headers (like clickjacking and XSS). It shows you what's missing, gives it a score out of 100, and a grade from A to F.
Headers it checks:
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Content-Security-Policy
- Referrer-Policy
- Permissions-Policy

## How it's built
Python + Flask for the backend, Tailwind for styling. Along the way I also added a few security basics, blocking requests to private/internal IPs, handling bad input without crashing, and rate limiting so it can't be spammed.

## Why I built it
I'm a CS student, and this is my first real project outside of coursework. No projects, no experience going in — just decided to actually build something instead of watching more tutorials. Hit a bunch of bugs along the way (shoutout to the 'UnboundLocalError' that took way longer to fix than it should've), but it works now.

## Try it
Live on: https://secure-head.onrender.com

## Running it yourself
```bash
git clone https://github.com/aleezakhannn/secure-head.git
cd secure-head
pip install -r requirements.txt
python app.py
```
then open 127.0.0.1:5000 in your browser.
