import unittest


class AssertMethods(unittest.TestCase):

    def assert_methods_in_test_case(self):

        testcase = "testcase"
        expected = "expected"

        self.assertEqual(testcase, expected)  # check that testcase == expected
        # self.assertNotEqual(testcase, expected)  # check that testcase != expected

        # self.assertTrue(testcase)  # check that bool(testcase) is True
        # self.assertFalse(testcase)  # check that bool(testcase) is False

        # self.assertIs(testcase, expected)  # check that testcase is expected
        # self.assertIsNot(testcase, expected)  # check that testcase is not expected

        # self.assertIsNone(testcase)  # check that testcase is None
        # self.assertIsNotNone(testcase)  # check that testcase is not None

        # self.assertIn(testcase, expected)  # check that testcase in expected
        # self.assertNotIn(testcase, expected)  # check that testcase not in expected

        # self.assertIsInstance(
        #     testcase, expected
        # )  check that isinstance(testcase, expected)
        # self.assertNotIsInstance(
        #     testcase, expected
        # )  check that not isinstance(testcase, expected)


if __name__ == "__main__":
    unittest.main()
