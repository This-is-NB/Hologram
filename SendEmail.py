import smtplib

def sendEmail(to, content):
    mail = "namanbansal.nbg@gmail.com"
    pas = "tuzudahanzoxugrr" #for gmail u have to generate an APP password due to security issues normal pass wont work
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(mail, pas)
    server.sendmail(mail, to, content)
    server.quit()
    
    
if __name__=="__main__":
    sendEmail("namanbansal.nbg@gmail.com", "hey there")