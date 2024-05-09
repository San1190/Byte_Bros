import unittest
import cambia_texto


class ProbarCambios(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'

        result = cambia_texto.todo_mayusculas(palabra)

        self.assertEqual(result,'BUEN DIA')


if __name__ == '__main__':
    unittest.main()