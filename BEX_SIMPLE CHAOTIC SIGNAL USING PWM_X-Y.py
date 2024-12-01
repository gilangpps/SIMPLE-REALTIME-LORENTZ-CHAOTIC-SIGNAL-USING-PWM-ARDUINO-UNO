import serial
import matplotlib.pyplot as plt
import time

# Hubungkan ke Arduino
ser = serial.Serial('COM6', 9600, timeout=1)  # Ganti 'COM6' dengan port Arduino Anda
time.sleep(2)  # Tunggu Arduino siap

# Buffer data Lorenz
data_x, data_y, data_z = [], [], []

# Baca data dari Arduino dan visualisasikan
try:
    plt.ion()
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    while True:
        try:
            # Baca data dari serial
            line = ser.readline().decode('utf-8').strip()
            if line:  # Pastikan data tidak kosong
                x, y, z = map(float, line.split(','))
                
                # Simpan data
                data_x.append(x)
                data_y.append(y)
                data_z.append(z)

                # Batasi jumlah data yang divisualisasikan
                if len(data_x) > 5000:
                    data_x.pop(0)
                    data_y.pop(0)
                    data_z.pop(0)

                # Visualisasikan data
                ax.clear()
                ax.plot(data_x, data_y, color='b', label='x-y')
                ax.set_title("Chaotic Signal Lorenz (x-y)")
                ax.set_xlabel("x")
                ax.set_ylabel("y")
                ax.legend()
                plt.pause(0.01)
        
        except ValueError:
            # Abaikan data yang tidak valid
            print("Data parsing error, skipping...")
            continue

except KeyboardInterrupt:
    print("Visualisasi selesai.")
finally:
    ser.close()
    plt.ioff()
    plt.show()
