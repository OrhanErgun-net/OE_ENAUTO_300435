import getpass
import telnetlib

HOST = "192.168.1.211"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"int gi2\n")
tn.write(b"ip add 10.10.10.2 255.255.255.0\n")
tn.write(b"no sh\n")
tn.write(b"end\n")
tn.write(b"wr\n")

print(tn.read_all().decode('ascii'))