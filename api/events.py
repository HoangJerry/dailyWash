from django_socketio import events, send

@events.on_connect()
def connection(request, socket, context):
    print "connection made successfully"
    send(socket.session.session_id, "Hello, new connection is established successfully")