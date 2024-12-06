from django.test import TestCase
from django.db import connection

class DatabaseConnectionTest(TestCase):
    def test_database_connection(self):
        """
        Testa se a conexão com o banco de dados está funcionando.
        """
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1;")
                result = cursor.fetchone()
                self.assertEqual(result[0], 1, "A conexão com o banco de dados falhou ou retornou um valor inesperado.")
        except Exception as e:
            self.fail(f"Erro ao conectar ao banco de dados: {e}")
