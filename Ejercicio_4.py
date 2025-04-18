# electrodomesticos.py

from datetime import datetime

class Electrodomestico:
    """Clase base para cualquier electrodoméstico."""
    def encender(self):
        """Mensaje genérico de encendido."""
        return "Encendiendo..."

class Lavadora(Electrodomestico):
    """Subclase que representa una lavadora."""
    def encender(self):
        """Mensaje personalizado al encender la lavadora."""
        return "Lavadora encendida. Iniciando ciclo de lavado."

class Television(Electrodomestico):
    """Subclase que representa una televisión."""
    def encender(self):
        """Mensaje personalizado al encender la televisión."""
        return "Televisión encendida. Mostrando canal principal."

class Refrigerador(Electrodomestico):
    """Subclase que representa un refrigerador."""
    def encender(self):
        """Mensaje personalizado al encender el refrigerador."""
        return "Refrigerador encendido. Enfriando compartimientos."

if __name__ == "__main__":
    # Fecha y hora actual para la evidencia
    ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Ejecución realizada el: {ahora}\n")

    # Crear instancias y mostrar mensajes
    dispositivos = [
        Electrodomestico(),
        Lavadora(),
        Television(),
        Refrigerador()
    ]
    nombres = [
        "Electrodoméstico genérico",
        "Lavadora",
        "Televisión",
        "Refrigerador"
    ]

    for nombre, dispositivo in zip(nombres, dispositivos):
        print(f"{nombre}: {dispositivo.encender()}")
