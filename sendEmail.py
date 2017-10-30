from time import sleep
import smtplib
import OLEDtext


import sys                  # need this to add a place to look for files
sys.path.append("/python")  # so it can go find the passwords file in the
import passwords            # parent directory.

fromEmail = passwords.passwords['helloboxun']
password = passwords.passwords['helloboxpw']
toEmail = passwords.passwords['helloboxsendto']


import passwords



def sendEmail(a,b):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromEmail, password)



    SUBJECT = a
    TEXT = b

    msg = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    #msg = "hey, motherfucker" 
    print msg

    server.sendmail(fromEmail, toEmail, msg)
    server.quit()

    OLEDtext.sending()
    
   
    
    # got this to auto-run by adding "sudo python /home/pi/Desktop/emailtest.py"
    # to /etc/profile

    
if __name__ == "__main__":
    sendEmail("bueno")