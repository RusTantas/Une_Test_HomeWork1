import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10


    def walk(self):
        self.distance += 5
        return self.distance

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runer = Runner("Test")
        for i in range(10):
            runer.walk()
        self.assertEqual(runer.distance, 50)

    def test_run(self):
        runer = Runner("Test2")
        for i in range(10):
            runer.run()
        self.assertEqual(runer.distance, 100)

    def test_challenge(self):
        runer1 = Runner("Runer1")
        runer2 = Runner("Runer2")
        for i in range(10):
            runer1.run()
            runer2.walk()
        self.assertNotEqual(runer1.distance, runer2.distance)

if __name__ == '__main__':
    unittest.main()
