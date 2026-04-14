# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():

    archivo = input("Nombre del archivo")

archivo = open(archivo, "r")
n = int(archivo.realice)

monitor = temp_monitor.init(n)

for i in range(n):
    temp = float(archivo.realice{})
    monitor = temp_monitor.add_realice(monitor, temp)

archivo.close()
print()

pass


if __name__ == "__main__":
    main()
