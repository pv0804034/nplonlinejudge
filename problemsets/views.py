from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound
from problemsets.models import Problem
from submissions.models import Submission
from programmers.models import Profile

from . import compiler as compiler
# import os

# Create your views here.

details = {-1: 'No status', 0: 'Solution accepted',
           1: 'Solution rejected', 2: 'Compilation error', 3: 'Runtime error', 4: 'Execution error', 5: 'Time-limit exceeded', 6: 'Memory-limit exceeded'}


def problems(request):
    ps = Problem.objects.order_by('id')
    if request.user.is_authenticated:
        uid = request.user.id
        for p in ps:
            s = Submission.objects.filter(userid=uid).filter(problemid=p.id)
            # check if submission has been made by user for the problem
            if len(s) > 0:
                # submission has been made
                p.solvestatus = 'Tried'
                solved = s.filter(status=0)
                if len(solved) > 0:
                    # at least once solved
                    p.solvestatus = 'Solved'
                    continue
            else:
                p.solvestatus = '-'
    return render(request, 'problemsets/problems.html', {'problems': ps})


def problemstmt(request, _id):
    # posted the problem
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
            # check the previous successful submission
            prevsub = Submission.objects.filter(userid=request.user.id).filter(
                problemid=_id).filter(status='0')
            submission = Submission(
                userid=userid, lang=lang, code=code, status=status, problemid=_id)
            submission.save()
            problem = problem[0]
            problem.attempts = problem.attempts + 1
            if status == 0:
                problem.successes = problem.successes + 1
                # if no previous success
                if len(prevsub) == 0:
                    profile = Profile.objects.filter(user_id=request.user.id)
                    if profile.exists():
                        # update the score with correct score
                        profile = profile[0]
                        profile.score = profile.score + problem.score
                        profile.save()
            # update the problemsets
            # increase the score if success
            problem.save()
            if remark == 0:
                messages.success(request, details[remark])
            else:
                messages.warning(request, details[remark])
        else:
            messages.warning(request, 'Required login to submit')
        return redirect('/submissions/{}/'.format(submission.id))
        # return render(request, 'submissions/submissiondetails.html', {'submission': res})
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
