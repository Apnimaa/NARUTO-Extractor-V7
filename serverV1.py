import getserver

def connect_server():
    server = getserver()
    server.connect_v1()

if __name__ == "__main__":
    connect_server()


