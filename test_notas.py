import unittest
from notas import estado, promedio, reporte, validar_nota


class TestNotas(unittest.TestCase):
    def test_promedio(self):
        self.assertEqual(promedio([16, 14, 12]), 14)
    def test_promedio_con_decimales(self):
        self.assertEqual(promedio([10, 9, 11]), 10)
        self.assertEqual(promedio([15, 16]), 15.5)
    def test_aprobado(self):
        self.assertEqual(estado(11), "Aprobado")
    def test_desaprobado(self):
        self.assertEqual(estado(10.9), "Desaprobado")
    def test_nota_fuera_de_rango(self):
        with self.assertRaises(ValueError):
            validar_nota(25)
    def test_estudiante_sin_notas(self):
        with self.assertRaises(ValueError):
            promedio([])
    def test_reporte(self):
        lineas = reporte({"Ana": [16, 14, 12]})
        self.assertIn("Aprobado", lineas[0])
        
if __name__ == "__main__":
    unittest.main()
