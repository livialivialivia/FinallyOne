#!/usr/bin/python
# _*_ coding: utf-8 _*_

import unittest
from SubmitReservation import SubmitReservation
from ChangeProcessing import ChangeProcessing
from ChangeStatus import ChangeStatus


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(SubmitReservation('test_submitreservation'))
    suite.addTest(ChangeProcessing('test_changeprocessing'))
    suite.addTest(ChangeStatus('test_changestatus'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
