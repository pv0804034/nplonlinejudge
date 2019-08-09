import subprocess
import os
import shutil


def compilation(user_id, lang, code, problemid):
    code = code.replace('\r\n', '\n')
    code.strip('\n')
    inputdir = 'io/input/input{}'.format(problemid)
    outputdir = 'io/output/output{}'.format(problemid)
    remark = 0
    ext = {'C': 'c', 'C++': 'cpp', 'Java': 'java', 'Python3': 'py'}
    filename = 'problem{}.{}'.format(problemid, ext[lang])
    absfilepath = 'submittedcodes/problem{}.{}'.format(
        problemid, ext[lang])
    with open(absfilepath, 'w') as wf:
        wf.write(code)
    if lang == 'Java':
        shutil.copy(absfilepath, 'submittedcodes/Main.java')
        filename = 'Main.java'
        absfilepath = 'submittedcodes/Main.java'
    if lang == 'C' or lang == 'C++':
        translator = 'gcc' if lang == 'C' else 'g++'
        compileobject = subprocess.run(
            [translator, '-o', 'executables/{filename}'.format(filename=filename), absfilepath])
        if compileobject.returncode != 0:
            remark = 2
        else:
            dirs = os.listdir(inputdir)
            inputfiles = sorted(dirs)
            l = len(inputfiles)
            for i in range(l):
                with open('{dir}/input{i}.txt'.format(dir=inputdir, i=i+1)) as rf:
                    systeminput = rf.read()
                try:
                    executeobject = subprocess.run(
                        ['executables/{filename}'.format(filename=filename)], input=systeminput.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
                except subprocess.TimeoutExpired:
                    remark = 5
                    break
                if executeobject.returncode != 0:
                    remark = 3
                    break
                else:
                    useroutput = executeobject.stdout.decode().rstrip()
                    with open('{}/output{}.txt'.format(outputdir, i+1), 'r') as rf:
                        sytemoutput = rf.read()
                    systemoutput = sytemoutput.rstrip()
                    if useroutput != systemoutput:
                        # output is incorrect
                        remark = 1
                        break
    elif lang == 'Java':
        ####################################################################################
        compileobject = subprocess.run(
            ['javac', '-d', 'executables', '{absfilepath}'.format(absfilepath=absfilepath)], stdout=subprocess.PIPE)
        if compileobject.returncode != 0:
            # compile error
            remark = 2
        else:
            # compilation successful
            dirs = os.listdir(inputdir)
            inputfiles = sorted(dirs)
            l = len(inputfiles)
            for i in range(l):
                with open('{dir}/input{i}.txt'.format(dir=inputdir, i=i+1)) as rf:
                    systeminput = rf.read()
                try:
                    executeobject = subprocess.run(
                        ['java', '-classpath', 'executables', '{filename}'.format(filename=filename.rstrip('.java'))], input=systeminput.encode(), stdout=subprocess.PIPE, timeout=1)
                except subprocess.TimeoutExpired:
                    remark = 5
                    break
                if executeobject.returncode != 0:
                    remark = 3
                    break
                else:
                    useroutput = executeobject.stdout.decode().rstrip()
                    with open('{}/output{}.txt'.format(outputdir, i+1), 'r') as rf:
                        sytemoutput = rf.read()
                    systemoutput = sytemoutput.rstrip()
                    if useroutput != systemoutput:
                        # output is incorrect
                        remark = 1
                        break
    elif lang == 'Python3':
        #################################################################################
        dirs = os.listdir(inputdir)
        inputfiles = sorted(dirs)
        l = len(inputfiles)
        allpassed = True
        for i in range(l):
            with open('{dir}/input{i}.txt'.format(dir=inputdir, i=i+1)) as rf:
                systeminput = rf.read()
            try:
                executeobject = subprocess.run(
                    ['python3', '{absfilepath}'.format(absfilepath=absfilepath)], input=systeminput.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=1)
            except subprocess.TimeoutExpired:
                remark = 5
                break
            if executeobject.returncode != 0:
                remark = 4
                break
            else:
                useroutput = executeobject.stdout.decode().rstrip()
                with open('{}/output{}.txt'.format(outputdir, i+1), 'r') as rf:
                    sytemoutput = rf.read()
                systemoutput = sytemoutput.rstrip()
                if useroutput != systemoutput:
                    # output is incorrect
                    remark = 1
                    break
    return remark
    # get next submission
    # evaluate the code and execute
    # register the submission to submissions table
