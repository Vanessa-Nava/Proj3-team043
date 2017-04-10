import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("proj.team43@gmail.com", "Teamproject43")

msg = "Test"
server.sendmail("proj.team43@gmail.com", "erickjacedo@gmail.com", msg)
server.quit()