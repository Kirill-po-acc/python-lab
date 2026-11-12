class ConnectDatabase:
    def __init__(self, port, hostname, username, password):
        self.port = port
        self.hostname = hostname
        self.username = username
        self.__password = password          # private (encapsulation)

    def show_connection(self):
        print("Hostname:", self.hostname)
        print("Port:    ", self.port)
        print("Username:", self.username)
        print("Password:", "*" * len(self.__password))   # hide the real password


if __name__ == "__main__":
    db = ConnectDatabase(5432, "localhost", "kirill", "secret123")
    db.show_connection()