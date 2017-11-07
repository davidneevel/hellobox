# test change
# the servo part of this relies on the pigpio library, 
# which relies on the pigpio daemon


import imaplib

import sys                  # need this to add a place to look for files
sys.path.append("/python")  # so it can go find the passwords file in the
import passwords            # parent directory.

fromEmail = passwords.passwords['helloboxun']
password = passwords.passwords['helloboxpw']

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(fromEmail,password)
mail.list()
import time
from time import sleep
from time import time

import OLEDtext
import servoshit
import buttons
import sendEmail
sendEmail.sendEmail("hellobox is running", "cool")

#servoshit.closeBox()


errors = 0
cycles = 0
prev_latest_email_id = 0
while True:
    try:
        mail.select("inbox")

        result, data = mail.search(None, "ALL")

        ids = data[0]  # data is a list
        id_list = ids.split()  # ids is a space separated string
        latest_email_id = id_list[-1]  # get the latest
        print "latest = %s" % (latest_email_id),
        # t = time.ctime()
        # print " checked at %s" % t,
        print " Cycles: %d" % cycles,
        print " Errors: %d" % errors

        if latest_email_id != prev_latest_email_id and cycles > 0:
            #result, data = mail. fetch(latest_email_id, "(RFC822)")  # fetch email body for the given id
            result, data = mail. fetch(latest_email_id, "(BODY[HEADER.FIELDS (SUBJECT)])")  # fetch email body for the given id

            subject = data[0][1]
            #getting the subject line of the email
            length = len(subject)
            subject = subject[9:length]

            servoshit.openBox()
            OLEDtext.display(subject)
            print subject
            buttons.buttons()

            servoshit.closeBox()
            sleep(.5)





        elif latest_email_id == prev_latest_email_id:
            print "No new mail"

        prev_latest_email_id = latest_email_id
        cycles += 1

        sleep(5)
    except():
        errors += 1
        sleep(15)