import sys;
import django
import os
import sqlparse
import pprint
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "classproject.settings")
from django.db.models import Count
from django.db.models import Avg
from django.db.models.functions import Coalesce
django.setup()
from onlineapp.models import*
def pq(qs):
     print sqlparse.format(str(qs.query),reindent=True)
def pp(qs):
    pprint.pprint(list(qs))

'''all colleges
count of colleges
get acronym and contact for each college
get college count in vizag
sort by acronym
sort by location desc
sort by location desc top 5
how many colleges in each location
colleges in each location sort by location
colleges in each location sort by num colleges desc
get acronym and contact for each college sorted by location
get colleges who have dropped out students
get colleges who do not have dropped out students'''
#c=College.objects.all()
#c=College.objects.all().count()
#c=College.objects.values_list("acronym","contact").order_by("acronym")
#c=College.objects.filter(location="vizag").count()
#c=College.objects.values("location").order_by("location").reverse()[:5]
#c=College.objects.values("location").annotate(Count("location"))
#c=College.objects.values("location").annotate(locate=Count("*")).order_by(("-locate"))
##c=College.objects.values("acronym","contact").annotate(locate=Count("*")).order_by("location")
#c=College.objects.filter(student__dropped_out=True).distict()
#c=College.objects.exclude(student__dropped_out=True)
#c=Student.objects.all().count()
#c=.filter(name__contains="rohit")
#c=.filter(college__acronym="bvritn")
#c=Student.objects.values("college__acronym").annotate(count=Count("*")).order_by("-count")
#c=College.objects.annotate(count=Count("student")).filter(count__gt=10)
#c=Student.objects.values("college__location").annotate(count=Count("*")).order_by("-count")
#pp(Student.objects.values("college__location").annotate(count=Count("*")).order_by("-count")[0])
c=MockTest1.objects.values("student__college__acronym").annotate(marks=Avg("total"),count=Count("*")).order_by("-marks")
pp(c)
p=College.objects.values("acronym").annotate(avg=Avg(Coalesce("student__mocktest1__total",0),count=Count("student"))).order_by("-avg")
pp(p)
#who are dropped out also
