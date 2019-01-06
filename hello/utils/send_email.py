import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("arbuzovfp@gmail.com", "MGTA2019")


def send_email(user_email, msg):
    try:
        server.sendmail('arbuzovfp@gmail.com', user_email, msg)
    except Exception as e:
        raise Exception
