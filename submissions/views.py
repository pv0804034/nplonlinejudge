from django.shortcuts import render
from submissions.models import Submission
from problemsets.models import Problem
from django.http import HttpResponseNotFound

# Create your views here.
statuses = {-1: 'No status', 0: 'Solution accepted',
            1: 'Solution rejected', 2: 'Compilation error', 3: 'Runtime error', 4: 'Execution error', 5: 'Time-limit exceeded', 6: 'Memory-limit exceeded'}


def submissiondetails(request, _id):
    userid = request.user.id
    res = Submission.objects.filter(userid=userid).filter(id=_id)
    if not res.exists():
        return HttpResponseNotFound()
    else:
        res = res[0]
        pname = Problem.objects.filter(id=res.problemid)[0]
        ptitle = pname.title
        ptag = pname.tag
        res.problemname = pname.title
        res.statusname = statuses[int(res.status)]
        res.problemtag = pname.tag
    return render(request, 'submissions/submissiondetails.html', {'submission': res})


def submissions(request):
    userid = request.user.id
    res = Submission.objects.filter(userid=userid).order_by('-id')
    for i in res:
        # print(i)
        # print(type(i))
        pname = Problem.objects.filter(id=i.problemid)[0]
        ptitle = pname.title
        ptag = pname.tag
        i.problemname = ptitle
        i.statusname = statuses[int(i.status)]
        i.problemtag = ptag
    # print(res)
    # submits = 'All submissions'
    return render(request, 'submissions/submissions.html', {'submissions': res})
