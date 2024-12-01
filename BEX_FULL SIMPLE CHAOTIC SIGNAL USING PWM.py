import serial
import matplotlib.pyplot as plt
import time

# Hubungkan ke Arduino
ser = serial.Serial('COM6', 9600, timeout=1)  # Ganti 'COM6' sesuai port Arduino
time.sleep(2)  # Tunggu Arduino siap

# Buffer data Lorenz
data_x, data_y, data_z = [], [], []

# Jumlah maksimum data yang ditampilkan
MAX_POINTS = 5000

# Baca data dari Arduino dan visualisasikan
try:
    plt.ion()
    fig, axes = plt.subplots(3, 1, figsize=(10, 12))  # Tiga subplot

    # Subplot untuk x-y, y-z, dan x-z
    ax_xy, ax_yz, ax_xz = axes
    ax_xy.set_title("Chaotic Signal Lorenz (x-y)")
    ax_xy.set_xlabel("x")
    ax_xy.set_ylabel("y")

    ax_yz.set_title("Chaotic Signal Lorenz (y-z)")
    ax_yz.set_xlabel("y")
    ax_yz.set_ylabel("z")

    ax_xz.set_title("Chaotic Signal Lorenz (x-z)")
    ax_xz.set_xlabel("x")
    ax_xz.set_ylabel("z")

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
                if len(data_x) > MAX_POINTS:
                    data_x.pop(0)
                    data_y.pop(0)
                    data_z.pop(0)

                # Clear setiap axis untuk memperbarui grafik
                ax_xy.clear()
                ax_yz.clear()
                ax_xz.clear()

                # Plot x-y
                ax_xy.plot(data_x, data_y, color='b', label='x-y')
                ax_xy.legend()

                # Plot y-z
                ax_yz.plot(data_y, data_z, color='g', label='y-z')
                ax_yz.legend()

                # Plot x-z
                ax_xz.plot(data_x, data_z, color='r', label='x-z')
                ax_xz.legend()

                # Refresh grafik
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
