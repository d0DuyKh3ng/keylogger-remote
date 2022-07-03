import socket

IP = "192.168.255.132"
PORT = 1234
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(ADDR)

	file = open("logs.txt", "r")
	data = file.read()

	client.send("logs.txt".encode(FORMAT))
	msg = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")

	client.send(data.encode(FORMAT))
	msg = client.recv(SIZE).decode(FORMAT)
	print(f"[SERVER]: {msg}")

	file.close()

	client.close()

if __name__ == "__main__":
	main()
