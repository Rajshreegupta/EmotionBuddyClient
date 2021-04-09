from django.shortcuts import render
import socket
# Create your views here.
class Chatting:
    def home(self, request):
        return render(request, 'connection.html')

    def add(self, request):
        host=request.POST["host"]
        self.s = socket.socket()
        port = 8080
        self.s.connect((host, port))
        incoming_message = self.s.recv(1024)
        incoming_message = incoming_message.decode()
        return render(request, 'home.html', {'msg_from_server': incoming_message})

    def receivemsg(self, request):
        incoming_message = self.s.recv(1024)
        incoming_message = incoming_message.decode()
        return render(request, 'home.html', {'msg_from_server': incoming_message})

    def sendmsg(self, request):
        message = request.POST["msg_from_client"]
        message = message.encode()
        self.s.send(message)
        incoming_message = self.s.recv(1024)
        incoming_message = incoming_message.decode()
        return render(request, 'home.html', {'msg_from_server': incoming_message})