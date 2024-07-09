import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
#from tests.homework.b_in_proc_out import tests_in_proc_out
from tests.examples.f_files_exception import tests_files_exception

suite = unittest.TestLoader().loadTestsFromModule(tests_files_exception)
unittest.TextTestRunner(verbosity=2).run(suite)
