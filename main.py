import lxml
import smtplib
from bs4 import BeautifulSoup
import requests
URL = PRODUCT_URL
EMAIL = SENDER_EMAIL_ADDRESS
PASSWORD = SENDER_EMAIL_PASSWORD
response = requests.get(URL,
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
                            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
                        }
                        )
web = response.text
soup = BeautifulSoup(web, "lxml")
price = float((soup.find(name="span", class_="a-price-whole").getText()).replace(",", ""))
message = f"{soup.find(name='span', id='productTitle').get_text().strip()} is now Rs {price}"
print(message)
if price <= 45000.0:
    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER_EMAIL_ADDRESS,
            msg=f"Subject: Amazon Price Alert\n\n{message}\n{URL}"
        )
