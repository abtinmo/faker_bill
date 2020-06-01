# faker-bill

[![Coverage Status](https://coveralls.io/repos/github/abtinmo/faker_bill/badge.svg?branch=master)](https://coveralls.io/github/abtinmo/faker_bill?branch=master)
[![Build Status](https://travis-ci.org/joke2k/faker.svg?branch=master)](https://travis-ci.org/joke2k/faker)
[![GitHub license](https://img.shields.io/github/license/abtinmo/faker_bill)](https://github.com/abtinmo/faker_bill/blob/master/LICENSE)

Provider for [Faker](https://faker.readthedocs.io/) which adds fake bill data.



install:

	pip install faker-bill

  
how to use:

	from faker import Faker
	from faker_bill.fa_IR import BillProvider
	fake = Faker('fa_IR')
	fake.add_provider(BillProvider)
	print(fake.bill_full())
		
	شرکت گاز

	قبض گاز

	bill id: 7734853606234

	payment id: 3004125788500

  
to run tests:

	python -m unittest tests/test_bill.py
