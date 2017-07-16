from search.scraper import *
from django.http import HttpResponse
from search.models import Tester

def renewdb():
	do = scrape("http://features.peta.org/cruelty-free-company-search/cruelty_free_companies_search.aspx?Dotest=8");
	dont = scrape("http://features.peta.org/cruelty-free-company-search/cruelty_free_companies_search.aspx?Donottest=8")
	Tester.objects.all().delete()
	insert(do, True)
	insert(dont, False)

def insert(data, stat):
	inserts = [];
	for row in data:
		if row["company"]:
			if row["parent"]:
				newRow = Tester(company=row["company"], parent=row["parent"], status=stat)
			else:
				newRow = Tester(company=row["company"], status=stat)
			inserts.append(newRow)
	if len(inserts) > 0:
		Tester.objects.bulk_create(inserts)