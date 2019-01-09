import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def Attach_Mail(file):
    fromaddr = "lakshyasukhralia1997@gmail.com"
    toaddr = "lakshyasukhralia97@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Issues Report"
    body = "PFA the report\n"+"\nRegards,\nTeam HK"
    msg.attach(MIMEText(body, 'plain'))
    #filename = "Lakshyasukhralia-CellularAutomata-issues.csv"
    filename = file
    attachment = open("D:\\HK Stuff\\%s"%filename, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, "********")
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()
