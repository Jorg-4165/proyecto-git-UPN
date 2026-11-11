"""Innovatec Education - Registro y cálculo de notas."""
NOTA_APROBATORIA = 11

def validar_nota(nota):
    if not 0 <= nota <= 20:
        raise ValueError(f"Nota inválida: {nota}. Debe estar entre 0 y 20")
    return nota
def promedio(notas):
    if not notas:
        raise ValueError("El estudiante no tiene notas")
    for nota in notas:
        validar_nota(nota)
    return round(sum(notas) / len(notas), 2)
def estado(prom):
    return "Aprobado" if prom >= NOTA_APROBATORIA else "Desaprobado"
def reporte(estudiantes):
    lineas = []
    for nombre, notas in estudiantes.items():
        prom = promedio(notas)
        lineas.append(f"{nombre:<15} {str(notas):<15} {prom:>6}   {estado(prom)}")
    return lineas
if __name__ == "__main__":
    estudiantes = {
        "Ana Torres": [16, 14, 12],
        "Luis Ramos": [10, 9, 11],
        "Maria Quispe": [18, 17, 19],
        "Jorge Carua": [15, 16, 14],
    }
    print("=== Innovatec Education - Reporte de notas ===")
    print(f"{'Estudiante':<15} {'Notas':<15} {'Prom.':>6}   Estado")
    for linea in reporte(estudiantes):
        print(linea)
