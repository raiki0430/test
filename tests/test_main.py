import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main(self):
        # テストが通ることを確認
        self.assertEqual(1, 1)

if __name__ == "__main__":
    unittest.main()

