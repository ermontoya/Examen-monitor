import psutil
import platform
from django.shortcuts import render

def sistema_info(request):
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disco = psutil.disk_usage('/')
        info = platform.uname()
        nucleos = psutil.cpu_count(logical=False)
        hilos = psutil.cpu_count(logical=True)

        datos = {
            'cpu': cpu,
            'ram_total': round(ram.total / (1024 ** 3), 2),
            'ram_usada': round(ram.used / (1024 ** 3), 2),
            'ram_porcentaje': ram.percent,
            'disco_total': round(disco.total / (1024 ** 3), 2),
            'disco_usado': round(disco.used / (1024 ** 3), 2),
            'disco_libre': round(disco.free / (1024 ** 3), 2),
            'disco_porcentaje': disco.percent,
            'sistema': info.system,
            'version': info.release,
            'nucleos': nucleos,
            'hilos': hilos,
        }

    except Exception as e:
        datos = {
            'error': 'Error al obtener datos del sistema.',
            'detalle': str(e)
        }

    return render(request, 'sistema/index.html', datos)

