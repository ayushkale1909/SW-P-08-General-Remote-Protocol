import socket
som = bytes([0x10, 0x02])
command = bytes([0x02])
eom = bytes([0x10, 0x03])
btc = 5
responses = {}
def calculate_byte_1(matrix, level):
    if not (0 < matrix <= 16) or not (0 < level <= 16):
        raise ValueError("Matrix and Level numbers between 1 and 16")
    value = (matrix - 1) << 4 | (level - 1)
    return value

def calculate_byte_2(source_number, dest_number):
    source_value = (source_number // 128) & 0b111
    dest_value = (dest_number // 128) & 0b111
    byte_value = (dest_value << 4) | source_value
    byte_value &= 0b01110111  
    return byte_value

def calculate_byte_3(dest_number):
    return dest_number % 128
def calculate_byte_4(source_number):
    return source_number % 128

def compute_checksum(data):
    total = sum(data) % 256
    return (256 - total) % 256

def send_message(message, ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(60)
        sock.connect((ip, port))
        print(f"Connected to {ip}:{port}")
        sock.send(message)
        print(f"Message sent.")
        reply = sock.recv(1024)
        print(f"Received reply: {reply}")
        time.sleep(1)
        reply = sock.recv(1024)
        print(f"Received reply: {reply}")
        time.sleep(1)
        reply = sock.recv(1024)
        print(f"Received reply: {reply}")
        time.sleep(1)
        
    except socket.timeout:
        print(f"Timeout: No reply received from {ip}:{port} within the set timeout period.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        sock.close()

ip_address = "192.168.10.28"
port_number = 62010

for matrix in range(1, 16):
    for level in range(1, 16):
        for source in range(1, 35):
            for dest in range(1, 35):
                byte_1_value = calculate_byte_1(matrix, level)
                byte_1 = bytes([byte_1_value])
                byte_2 = calculate_byte_2(source, dest)
                byte_3 = calculate_byte_3(dest)
                byte_4 = calculate_byte_4(source) 
                chk_data = command + byte_1 + bytes([byte_2, byte_3,byte_4, btc])
                chk = compute_checksum(chk_data)
                message = som + command + byte_1 + bytes([byte_2, byte_3,byte_4, btc, chk]) + eom
                key = (matrix, level, source, dest)
                response = send_message(message, ip_address, port_number)
                responses[key] = response
                


for key, value in responses.items():
    print(f"Key: {key}, Response: {value}")
