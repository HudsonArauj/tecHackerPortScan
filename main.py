import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    target = entry_host.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())

    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        
        if result == 0:
            service = get_service_name(port)
            messagebox.showinfo("Port Open", f"Port {port} ({service}) is open")

def get_service_name(port):
    well_known_ports = {
        20: "FTP (Data)",
        21: "FTP (Control)",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        143: "IMAP",
    }
    return well_known_ports.get(port, "Unknown")


# Interface gráfica
root = tk.Tk()
root.title("Port Scanner")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_host = tk.Label(frame, text="Host:")
label_host.grid(row=0, column=0, sticky="w")
entry_host = tk.Entry(frame)
entry_host.grid(row=0, column=1)

label_start_port = tk.Label(frame, text="Start Port:")
label_start_port.grid(row=1, column=0, sticky="w")
entry_start_port = tk.Entry(frame)
entry_start_port.grid(row=1, column=1)

label_end_port = tk.Label(frame, text="End Port:")
label_end_port.grid(row=2, column=0, sticky="w")
entry_end_port = tk.Entry(frame)
entry_end_port.grid(row=2, column=1)

button_scan = tk.Button(frame, text="Scan Ports", command=scan_ports)
button_scan.grid(row=3, columnspan=2)

root.mainloop()

