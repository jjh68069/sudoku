import unittest
from app import create_app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_hello(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")


if __name__ == "__main__":
    unittest.main()
