import socket

IP = "0.0.0.0"
PORT = 1234
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024


def main():
	print("[STARTING] Server Đang Bắt Đầu.")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(ADDR)
	server.listen()
	print("[LISTENING] Server Đang Bắt Đầu Lắng Nghe.")

	while True:
		conn, addr = server.accept()
		print(f"[NEW CONNECTION] {addr} Đã Kết Nối.")

		filename = conn.recv(SIZE).decode(FORMAT)
		print("[RECV] Đang lấy tên File.")
		file = open(filename, "w")
		conn.send("Đã nhận được tên File.".encode(FORMAT))

		data = conn.recv(SIZE).decode(FORMAT)
		print(f"[RECV] Đang nhận dữ liệu.")
		file.write(data)
		conn.send("Đã nhận được dữ liệu.".encode(FORMAT))

if __name__ == "__main__":
        main()

