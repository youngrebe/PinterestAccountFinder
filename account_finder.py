import undetected_chromedriver as uc
import sys
from lib import email_converter
from lib import cli
import time

# ====== EMAIL ====== #
email = input("Target email: ")
username = email_converter.clean_email(email)

# ====== DRIVER ====== #
OPTIONS = uc.ChromeOptions()
OPTIONS.add_argument('--headless')
DRIVER = uc.Chrome(options=OPTIONS)

# ====== PINTEREST ====== #
DRIVER.get(f"https://pinterest.com/{username}")
time.sleep(5)

if DRIVER.current_url.endswith("?show_error=true"):
    cli.separator_line(40)
    print("\nThere is no account with such an email.\n")
    cli.separator_line(40)
    sys.exit()

cli.separator_line(40)
print(f"\nProfile: {DRIVER.current_url}\n")
cli.separator_line(40)

