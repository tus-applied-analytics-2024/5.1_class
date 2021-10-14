# -*- coding: utf-8 -*-
from main import LinearRegression
import unittest
import numpy as np

class TestCase(unittest.TestCase):

    def assertAllClose(self, a, b, rtol=1e-5, atol=1e-8):
        self.assertTrue(np.allclose(a, b, rtol=rtol, atol=atol))

    def test_class(self):
        model = LinearRegression(dim=5)
        self.assertAllClose(model.w, np.array([1, 1, 1, 1, 1]))

        for _ in range(10):
            X = np.random.randn(10, 5)
            self.assertAllClose(X @ np.array([1, 1, 1, 1, 1]),
                                model.predict(X))


if __name__ == "__main__":
    unittest.main()
