from django.shortcuts import render
from search.models import Tester
import search.utils
import json

# Create your views here.
def index(request):
	testerSet = Tester.objects.all().order_by("company")
	testerList = []
	for tester in testerSet:
		if tester.parent:
			#Use brackets on parent to make search more clear
			record = { "company": tester.company, "parent": "("+tester.parent+")", "status": tester.status, "timestamp": tester.updated.date().strftime('%d/%m/%Y') }
		else:
			record = { "company": tester.company, "parent": "", "status": tester.status, "timestamp": tester.updated.date().strftime('%d/%m/%Y') }
		testerList.append(record)
	return render(request, 'search/home.html', {"json": json.dumps( testerList )})

def renewdb(request):
	search.utils.renewdb()
	return render(request, 'search/renewdb.html')