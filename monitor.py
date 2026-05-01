import subprocess 
import platform    
import datetime    

hosts = [
    "8.8.8.8",        
    "1.1.1.1",        
    "google.com",     
    "192.168.1.1",    
]

def hacer_ping(host):
    """
    Hace ping a un host y devuelve True si responde, False si no.
    """
    if platform.system() == "Windows":
        comando = ["ping", "-n", "1", "-w", "1000", host]
    else:
        comando = ["ping", "-c", "1", "-W", "1", host]
    
    resultado = subprocess.run(
        comando,
        stdout=subprocess.DEVNULL, 
        stderr=subprocess.DEVNULL
    )
    
    return resultado.returncode == 0
    
print("=" * 40)
print("   MONITOR DE RED - Estado de Hosts")
print("=" * 40)

hora_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Hora del escaneo: {hora_actual}\n")

for host in hosts:
    activo = hacer_ping(host)
    
    if activo:
        estado = "✅ ACTIVO"
    else:
        estado = "❌ CAÍDO"
    
    print(f"{host:<20} → {estado}")

print("\n" + "=" * 40)
print("Escaneo completado.")
