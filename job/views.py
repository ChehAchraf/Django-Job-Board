from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.
def job_list(reqeust):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render(reqeust, 'job/jobs.html',context)

def job_details(reqeust,id):
    job_detail = Job.objects.get(id=id)
    context = {'job' : job_detail, 'id' : id}
    return render(reqeust, 'job/job_details.html',context)