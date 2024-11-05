## UNITTEST AND INTEGRATION TESTS
 - The unittest module provides a rich set of tools for constructing and running tests. This section demonstrates that a small subset of hte tools suffice to meet the needs of the most users.

  - Here is a short script to test three string methods
    
    ``` 
    import unittest

    class TestStringMethods(unittest.TestCase):

        def test_upper(self):
            self.assertEqual('foo'.upper(), 'FOO')

        def test_isupper(self):
            self.assertTrue('FOO'.isupper())
            self.assertFalse('Foo'.isupper())

        def test_split(self):
            s = 'hello world'
            self.assertEqual(s.split(), ['hello', 'world'])
            # check that s.split fails when the separator is not a string
            with self.assertRaises(TypeError):
                s.split(2)

    if __name__ == '__main__':
        unittest.main()
    
    ```
 A test case is created by subclassing `unittest.TestCase`. The three individual tests are defined with methods whose names start with the letters test. This naming convention informs the test runner about which methods represent tests.

 The crux of each test is a call to `assertEqual()` to check for an expected result; `assertTrue()` or `assertFalse()` to verify a condition; or `assertRaise()` to verify that a specific exception gets raised. These methods are used instead of the assert statement so the test runner can accumulate all test results and produce a report.

 The `setUp()` and `tearDown()` methods allow you to define instructions that will be executed before and after each test method.

 The `unittest.main()` provides a command-line interface to the test script. when run from the command-line, the above script produces an output that looks like this:

    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.000s

    OK

