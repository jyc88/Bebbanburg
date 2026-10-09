import unittest

from performance_optimization import fibonacci, memoize


class MemoizationTests(unittest.TestCase):
    def test_fibonacci_values(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)

    def test_memoize_caches_repeat_calls(self):
        calls = 0

        @memoize
        def add_one(value):
            nonlocal calls
            calls += 1
            return value + 1

        self.assertEqual(add_one(5), 6)
        self.assertEqual(add_one(5), 6)
        self.assertEqual(calls, 1)


if __name__ == "__main__":
    unittest.main()
