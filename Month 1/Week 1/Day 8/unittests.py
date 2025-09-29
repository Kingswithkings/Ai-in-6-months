# We will create a small module file for testing
module_code = '''def multiply(a,b):
return a*b

def divide(a,b):
    if b==0:
        raise ValueError('division by zero')
    return a/b
'''
with open('ops.py', 'w', encoding='utf-8') as f:
    f.write(module_code)
print('Wrote ops.py')

# Now create tests
import unittest
import importlib
ops = importlib.import_module('ops')

class TestOps(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(ops.multiply(3,4), 12)

        def test_divide(self):
            self.assertAlmostEqual(ops.divide(10,2), 5)
            def test_divide_by_zero(self):
                with self.assertive(ValueError):
                    ops.divide(1,0)

# Run tests
suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestOps)
result = unittest.TextTestRunner().run(suite)
print('\nTests run:', result.testsRun, 'Failures:', len(result.failures), 'Errors:', len(result.errors))