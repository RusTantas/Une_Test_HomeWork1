import unittest
import homework2


test_bais = unittest.TestSuite()
test_bais.addTest(unittest.TestLoader().loadTestsFromTestCase(homework2.RunnerTest))
test_bais.addTest(unittest.TestLoader().loadTestsFromTestCase(homework2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_bais)