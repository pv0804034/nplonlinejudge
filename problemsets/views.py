from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from problemsets.models import Problem
from submissions.models import Submission

from . import compiler as compiler
# import os

# Create your views here.

details = {-1: 'No status', 0: 'Solution accepted',
           1: 'Solution rejected', 2: 'Compilation error', 3: 'Runtime error', 4: 'Execution error', 5: 'Time-limit exceeded', 6: 'Memory-limit exceeded'}


def problems(request):
    return render(request, 'problemsets/problems.html', {'problems': Problem.objects.all()})


def problemstmt(request, _id):
    if request.method == 'POST':
        # post request
        problem = Problem.objects.filter(id=_id)
        if not problem.exists():
            return HttpResponseNotFound()
        if request.user.is_authenticated:
            # authentic user
            # evaluate the submission
            remark = compiler.compilation(
                request.user.id, request.POST['lang'], request.POST['code'], _id)
            # messages.success(
            #     request, 'Submission successful')
            userid = request.user.id
            lang = request.POST['lang']
            code = request.POST['code']
            status = remark
            submission = Submission(
                userid=userid, lang=lang, code=code, status=status, problemid=_id)
            submission.save()
            problem = problem[0]
            problem.attempts = problem.attempts + 1
            if status == 0:
                problem.successes = problem.successes + 1
            # update the problemsets
            problem.save()
            if remark == 0:
                messages.success(request, details[remark])
            else:
                messages.warning(request, details[remark])
        else:
            messages.warning(request, 'Required login to submit')
        return redirect('/problemsets/{}/'.format(_id))
    else:
        # get request
        # with open('io/problem{}.html'.format(_id), 'r') as rf:
        #     stmt = rf.read()
        problem = Problem.objects.filter(id=_id)
        if not problem.exists():
            return HttpResponseNotFound()
        else:
            problem = problem[0]
        return render(request, 'problemsets/problemstmt.html', {'problem': problem})
