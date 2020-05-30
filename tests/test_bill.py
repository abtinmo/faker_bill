import re
import unittest

from faker import Faker

from faker_bill.fa_IR import BillProvider


def check_bill_id(bill_id):
    """ Check if bill match the bill id algorithm """
    j = 0
    sum_of_numbers = 0
    codes = [2, 3, 4, 5, 6, 7]
    if len(bill_id) <= 11:
        return False
    length = len(bill_id)
    i = length - 2
    while i >= 0:
        sum_of_numbers += int(bill_id[i]) * codes[j]
        if j < 5:
            j += 1
        else:
            j = 0
        i -= 1

    i = sum_of_numbers % 11
    if i > 1:
        i = 11 - i
    else:
        i = 0
    if int(bill_id[length - 1]) != i:
        return False
    return True


class TestBillFaIrProvider(unittest.TestCase):
    """ Test bill in fa_IR locale """

    def setUp(self):
        self.fake = Faker('fa-IR')
        self.fake.add_provider(BillProvider)

    def test_bill_name(self):
        bill_name = self.fake.bill_name()
        assert re.match("^[\u0600-\u06FF ]+$", bill_name)


    def test_bill_provider(self):
        provider = self.fake.bill_provider()
        assert re.match("^[\u0600-\u06FF ]+$", provider)

    def test_provider_name(self):
        bill_provider = self.fake.bill_name()
        assert re.match("^[\u0600-\u06FF ]+$", bill_provider)

    def test_bill_id(self):
        bill_id = self.fake.bill_id()
        assert isinstance(bill_id, str)
        assert check_bill_id(bill_id)

    def test_payment_id(self):
        payment_id = self.fake.bill_payment_id()
        assert isinstance(payment_id, str)

    def test_full(self):
        bill_full = self.fake.bill_full()
        assert isinstance(bill_full, str)
