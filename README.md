# PinterestAcccountFinder

PinterestAccountFinder is a simple Python tool for finding Pinterest profiles associated with a given email address. It helps you quickly locate a user's profile by entering their email.

## Installation and Usage

Run account_finder.py and enter the target email token.

```bash
# Git
git clone https://github.com/youngrebe/PinterestAcccountFinder.git
cd PinterestAcccountFinder

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate # LINUX
venv/Scripts/activate # WINDOWS

# Install dependencies
pip install -r requirements.txt

# Upgrade setuptools (required for undetected_chromedriver)
pip install --upgrade setuptools

# Run the script
python3 account_finder.py
```

Enter the target email when prompted

## Examples
```bash
python account_finder.py
Target email: mihaillobacev3@gmail.com
----------------------------------------

Profile: https://ru.pinterest.com/rarrepon/

----------------------------------------
```