import pandas as pd

print("=== SISTEMA DE SOLICITUD DE VACACIONES ===")

try:
    empleados = pd.read_excel("empleados.xlsx")

    dni = input("Ingrese su DNI: ").strip()

    if not dni.isdigit():
        print("Error: Debe ingresar solo números.")
    else:
        empleado = empleados[empleados["DNI"].astype(str) == dni]

        if empleado.empty:
            print("Error: DNI no encontrado.")
        else:
            nombre = empleado.iloc[0]["NOMBRE"]
            dias = int(empleado.iloc[0]["DIAS"])

            print(f"\nEmpleado: {nombre}")
            print(f"Días disponibles: {dias}")

            if dias > 0:
                print("Solicitud APROBADA")
            else:
                print("Solicitud RECHAZADA")
                print("No posee días disponibles.")

except FileNotFoundError:
    print("No se encontró el archivo empleados.xlsx")