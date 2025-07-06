
import socket
import time

def ping_mc_server(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"✔ Server {host}:{port} phản hồi thành công.")
            return True
    except Exception as e:
        print(f"✘ Lỗi khi kết nối tới {host}:{port} → {e}")
        return False

if __name__ == "__main__":
    print("💡 Nhập IP server Minecraft cần kiểm tra:")
    host = input("🖥 IP: ").strip()

    port_input = input("🔌 Port (mặc định 25565): ").strip()
    port = int(port_input) if port_input else 25565

    print(f"🚀 Bắt đầu kiểm tra hiệu năng server {host}:{port}... (bấm Ctrl+C để dừng)")
    count = 0
    while True:
        count += 1
        print(f"[Lần ping thứ {count}]")
        ping_mc_server(host, port)
        time.sleep(0.5)
