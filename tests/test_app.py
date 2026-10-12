import unittest
from app import app


class AppTest(unittest.TestCase):
    def test_homepage(self):
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
