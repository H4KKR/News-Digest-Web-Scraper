import requests, smtplib, time
from bs4 import BeautifulSoup

headline = ""
URL = 'https://www.bbc.co.uk/news'
your_email = input("Enter your email address: ")
your_pass = input("Enter your app password: ")
their_email = input("Enter the email of who to send the email to: ")
def get_headline():
    global headline

    page = requests.get(URL, 'html.parser')
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(attrs={'class': 'gs-c-promo-heading__title'}).get_text().strip()
    breif = soup.find(attrs={'class': 'gs-c-promo-summary'}).get_text().strip()
    print(title)
    if title != headline:
        headline = title
        send_mail(title, breif)
    else:
        print('\n\n NEWS NOT CHANGED!! \n\n')

def send_mail(title, breif):
    global your_email
    global your_pass
    global their_email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(your_email, your_pass)

    subject = "BREAKING NEWS!"
    body = str(title) + "\n\n" + str(breif) +  " \n\nURL = www.bbc.co.uk/news"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        your_email,
        their_email,
        msg
    )
    print("Breaking news sent")
    server.quit()

while True:
    get_headline()
    time.sleep(600)
