# import smtplib
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText
# from email.MIMEBase import MIMEBase
# from email import encoders
 
# fromaddr = "YOUR EMAIL"
# toaddr = "EMAIL ADDRESS YOU SEND TO"
 
# msg = MIMEMultipart()
 
# msg['From'] = fromaddr
# msg['To'] = toaddr
# msg['Subject'] = "SUBJECT OF THE EMAIL"
 
# body = "TEXT YOU WANT TO SEND"
 
# msg.attach(MIMEText(body, 'plain'))
 
# filename = "NAME OF THE FILE WITH ITS EXTENSION"
# attachment = open("PATH OF THE FILE", "rb")
 
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((attachment).read())
# encoders.encode_base64(part)
# part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
# msg.attach(part)
 
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(fromaddr, "YOUR PASSWORD")
# text = msg.as_string()
# server.sendmail(fromaddr, toaddr, text)
# server.quit()
#**************************************************************************************************

import smtplib, socket, sys, getpass

def main():
    print 
    
    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpsever.starttls()
        smtpserver.ehlo()
        print ('Connection to Gmail Successfull')
        print ('Connected to Gmail!') + "\n"
        try:
            gmail_user = str(raw_input('Enter your Gmail : ')).lower().strip()
            gmail_pwd = getpass.getpass('Enter your Email password: ').strip
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print ('Authentication failed.') + '\n'
            smptserver.close
            smtpserver.getpass('Press ENTER to continue ... ')
            sys.exit(1)
                
    except smtplib.SMTPException:
        print ('Connection to Gmail Failed')
        getpass.getpass('Press ENTER to continue ... ')
        
    print ('\n')
    raw_input('pause program')