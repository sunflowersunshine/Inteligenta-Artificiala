from hashlib import new
import requests
from bs4 import BeautifulSoup
import smtplib

sender_email = "nu_vreau_spam@coneasorin.ro"
subject = "Pretul a scazut la :"
to_addr_list = ['monicastoleru7@gmail.com']
cc_addr_list = ['']


def send_mail(sender_email, message, subject, to_addr_list, cc_addr_list=[]):

    try:
        smtpserver = "mail.x-it.ro:26"
        header = 'From: %s\n' % sender_email
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'CC: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender_email, "stiinte216_2022")
        problems = server.sendmail(sender_email,  to_addr_list, message)
        server.quit()
        return True
    except:
        print("Error:unable to send email")
        return False


def data_scraping():
    req = requests.get(
        "https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-256gb-5g-deep-purple-mq9x3rx-a/pd/DJDY4LMBM/")
    soup = BeautifulSoup(req.text, 'html.parser')
    price = soup.find('p', attrs={'class': 'product-new-price'}).text
    print(price)
    pret = int(price[0:5].replace(".", ""))

    if (pret < 8000):
        send_mail(sender_email, "Pretul a scazut la: " + str(pret),
                  subject, to_addr_list, cc_addr_list=[])


data_scraping()
