## Sample server
import socket
import argparse
import time

def send_data(host, port, messages):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Connected to {host}:{port}")

            for message in messages:
                print(f"Sending: {message}")
                data = (message + '\n').encode('utf-8')
                s.sendall(data)

                time.sleep(0.1)

            print("All messages sent. Closing the connection.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Send data to a specified IP and port.")
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host IP address')
    parser.add_argument('--port', type=int, default=8080, help='Port number')
    args = parser.parse_args()

    messages = [
        "Hello, server!",
        "This is a test message.",
        "Sending some data.",
        "Hope you're receiving this!",
        "Goodbye!"
    ]

    send_data(args.host, args.port, messages)

if __name__ == "__main__":
    main()
