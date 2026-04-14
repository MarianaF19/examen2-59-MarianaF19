# temp_monitor_client.py
# Programa cliente que lee temperaturas de un archivo
# e imprime la racha creciente mas larga.

import temp_monitor


def main():
   
    archivochivo = input("Nombre del archivo: ")
    
    archivo = open(archivo, 'r')
    n = int(archivo.readline())
    
    monitor = temp_monitor.init(n)
    
    for i in range(n):
        temp = float(archivo.readline())
        monitor = temp_monitor.add_reading(monitor, temp)
    
    archivo.close()
    print(temp_monitor.longest_rising_streak(monitor))
    
    pass


if __name__ == "_main_":
    main()