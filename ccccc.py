import ftplib


q = ftplib.FTP()
q.connect("localhost",2121)
q.login('user','12345')
data = []
q.dir(data.append)
q.quit()

for line in data:
    print("-", line)
