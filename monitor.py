# monitor.py
# Proyecto: Monitor de Ping
# Descripción: Verifica si una lista de hosts están activos o caídos

import subprocess  # Para ejecutar comandos del sistema
import platform    # Para detectar si estamos en Windows o Linux/Mac
import datetime    # Para mostrar la hora actual

# ---- CONFIGURACIÓN ----
# Agrega aquí las IPs o sitios que quieres monitorear
hosts = [
    "8.8.8.8",        # Google DNS
    "1.1.1.1",        # Cloudflare DNS
    "google.com",     # Sitio web
    "192.168.1.1",    # Tu router (puedes cambiar esta IP)
]

# ---- FUNCIÓN PRINCIPAL ----
def hacer_ping(host):
    """
    Hace ping a un host y devuelve True si responde, False si no.
    """
    # El comando de ping es diferente en Windows vs Linux/Mac
    if platform.system() == "Windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    
    # Ejecutamos el comando y capturamos el resultado
    resultado = subprocess.run(
        comando,
        stdout=subprocess.DEVNULL,  # Ocultamos la salida del ping
        stderr=subprocess.DEVNULL
    )
    
    # Si el código de salida es 0, el host respondió
    return resultado.returncode == 0


# ---- PROGRAMA PRINCIPAL ----
print("=" * 40)
print("   MONITOR DE RED - Estado de Hosts")
print("=" * 40)

hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Hora del escaneo: {hora_actual}\n")

# Recorremos cada host y hacemos ping
for host in hosts:
    activo = hacer_ping(host)
    
    if activo:
        estado = "✅ ACTIVO"
    else:
        estado = "❌ CAÍDO"
    
    print(f"{host:<20} → {estado}")

print("\n" + "=" * 40)
print("Escaneo completado.")