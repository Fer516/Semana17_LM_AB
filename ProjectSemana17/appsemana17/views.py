from django.shortcuts import render
from .models import Venta, Empleado, Area, Cliente

def Lista(request):
    ventas_listado = Venta.objects.all()
    empleados_listado = Empleado.objects.all()
    areas_listado = Area.objects.all()
    clientes_listado = Cliente.objects.all()

    return render(
        request,
        "prueba.html",
        {
            "ventas": ventas_listado,
            "empleados": empleados_listado,
            "areas": areas_listado,
            "clientes": clientes_listado,
        },
    )
