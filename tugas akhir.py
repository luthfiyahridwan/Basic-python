import smtplib  #module yang digunakan untuk mengirim email
from email.mime.multipart import MIMEMultipart  #untuk munjukan kalau ada lebih dari 1 part
from email.mime.text import MIMEText  #format email mendukung teks serta lampiran audio, video, gambar, dan program

dari = "firecracker.bing@gmail.com"
recepients = ["ridwanluthfiyah@gmail.com", "anselacool@gmail.com"]
msg = MIMEMultipart()
msg['From'] = dari
msg['To'] = ', '.join(recepients)
msg['Subject'] = "Nyoba yang baru"

body = "Hello, test test\n" "Coba bisa gak"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()  #untuk menempatkan koneksi dari server SMTP ke mode TLS
server.login(dari, "Iniajadulu12")
text = msg.as_string()
server.sendmail(dari, recepients, text)
server.quit()

'''
sources
https://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python
'''