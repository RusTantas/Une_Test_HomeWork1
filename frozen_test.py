import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, '����� � ���� ����� ����������')
    def test_walk(self):
        object_runner = runner.Runner('Alex')
        for i in range(10):
            object_runner.walk()
        self.assertEqual(object_runner.distance, 50)

    @unittest.skipIf(is_frozen == False, '����� � ���� ����� ����������')
    def test_run(self):
        object_runner = runner.Runner('Sofia')
        for i in range(10):
            object_runner.run()
        self.assertEqual(object_runner.distance, 100)

    @unittest.skipIf(is_frozen == False, '����� � ���� ����� ����������')
    def test_challenge(self):
        object_runner_1 = runner.Runner('Paul')
        object_runner_2 = runner.Runner('Dominik')
        for i in range(10):
            object_runner_1.walk()
            object_runner_2.run()
        self.assertNotEqual(object_runner_1.distance, object_runner_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = None

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        res = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                res[k] = str(v)
            print(res)

    def setUp(self):
        self.usain = runner_and_tournament.Runner('�����', 10)
        self.andrew = runner_and_tournament.Runner('������', 9)
        self.nick = runner_and_tournament.Runner('���', 3)

    @unittest.skipIf(is_frozen == True, '����� � ���� ����� ����������')
    def test_run_first(self):
        first_run = runner_and_tournament.Tournament(90, self.usain, self.nick)
        result = first_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == '���')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, '����� � ���� ����� ����������')
    def test_run_second(self):
        second_run = runner_and_tournament.Tournament(90, self.andrew, self.nick)
        result = second_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == '���')
        self.all_results[result.values()] = result

    @unittest.skipIf(is_frozen == True, '����� � ���� ����� ����������')
    def test_run_third(self):
        third_run = runner_and_tournament.Tournament(90, self.andrew, self.usain, self.nick)
        result = third_run.start()
        last_runner = list(result.values())
        self.assertTrue(last_runner[-1] == '���')
        self.all_results[result.values()] = result


if __name__ == '__main__':
    unittest.main()