import os
from flask import Flask, session, render_template, url_for, redirect, request, flash
from copy import deepcopy
from datetime import datetime, date, time
from random import choice, shuffle, sample
# Create a flask app and set its secret key
app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
'0': {'answer': 'theFunction.__name__',
      'question': 'Which of the following is the correct way to output the name of any function (including builtin functions) using Python?',
      'options': ['theFunction.__func_name__', 'theFunction.func_name', 'theFunction.__name__', 'theFunction.name()']},
'1': {'answer': 'thelist[3:]',
      'question': "For the list 'thelist = [1, 2, 3, 4, 5]', how could the last two elements of the list (4,5) be selected using slices?",
      'options': ['thelist[3:]', 'thelist[-2]', 'thelist[3:4]', 'thelist[3,4]']},
'2': {'answer': 'Put __init__.py file in the module path and import it using the import statement',
      'question': 'Which option will import a module which is not in PYTHONPATH or the current directory?',
      'options': ['Put __init__.py file in the module path and import it using the import statement','import <modulename>', 'Add the path in program by sys.path.insert(<path>)', '<modulename> import *']},
'3': {'answer': 'installtools', 'question': 'Which is not used to install Python packages?',
      'options': ['installtools', 'easy_install', 'distribute', 'pip']},
'4': {'answer': "Do not bind to a specific port, or bind to port 0, e.g. sock.bind(('',0))",
      'question': 'Which is correct about getting a free port number?',
      'options': ["Do not bind to a specific port, or bind to port 0, e.g. sock.bind(('',0))", 'use sock.getsockname() to get a free port number', 'We cannot get a free port number', "Directly use a desired port number in bind function,e.g. sock.bind(('',port_number))"]},
'5': {'answer': 'sys.stdin',
      'question': 'Which user input method will act like a file-object on which read and readline function can be called',
      'options': ['input()', 'sys.argv', 'sys.stdin', 'raw_input()']},
'6': {'answer': '__floordiv__()',
      'question': 'Which function overloads the // operator?',
      'options': ['__truediv__()', '__radd__', '__floordiv__()', '__ceildiv__()']}
}
#
py_summary={}
py_summary["correct"]=[]
py_summary["wrong"]=[]
py_summary["curretq"]=1
Qs = sample(range(len(questions)-1),3)

app.nquestions=len(questions)

for item in questions.keys():
   shuffle(questions[item]['options'])   

@app.route('/trivia', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        #Question 1:
        check_ans_1 = request.form.get('answer_python_1','')
        if not check_ans_1:
            py_summary["wrong"].append(questions[str(Qs[0])]['question'])

        else:
            answer_1 = request.form['answer_python_1']
            correct_answer_1 = questions[str(Qs[0])]["answer"]

            if answer_1 == correct_answer_1[:len(answer_1)]:
                py_summary["correct"].append(questions[str(Qs[0])]['question'])
        
            else:
                py_summary["wrong"].append(questions[str(Qs[0])]['question'])
		
        #Question 2:
        check_ans_2 = request.form.get('answer_python_2')
        if not check_ans_2:
            py_summary["wrong"].append(questions[str(Qs[1])]['question'])

        else:                          
            answer_2 = request.form['answer_python_2']
            correct_answer_2 = questions[str(Qs[1])]["answer"]
    
            if answer_2 == correct_answer_2[:len(answer_2)]:
                py_summary["correct"].append(questions[str(Qs[1])]['question'])
        
            else:
                py_summary["wrong"].append(questions[str(Qs[1])]['question'])

        #Question 3:
        check_ans_3 = request.form.get('answer_python_3')
        if not check_ans_3:
            py_summary["wrong"].append(questions[str(Qs[1])]['question'])

        else:
            answer_3 = request.form['answer_python_3']
            correct_answer_3 = questions[str(Qs[2])]["answer"]
    
            if answer_3 == correct_answer_3[:len(answer_3)]: 
                py_summary["correct"].append(questions[str(Qs[2])]['question'])
        
            else:
                py_summary["wrong"].append(questions[str(Qs[2])]['question'])
                
        Q_1 =  questions[str(Qs[0])]["question"]
        a1_1, a2_1, a3_1,a4_1 = questions[str(Qs[0])]["options"] 
        Q_2 = questions[str(Qs[1])]["question"]
        a1_2, a2_2, a3_2,a4_2 = questions[str(Qs[1])]["options"]
        Q_3 = questions[str(Qs[2])]["question"]
        a1_3, a2_3, a3_3,a4_3 = questions[str(Qs[2])]["options"]
        py_summary["wrong"]=list(set(py_summary["wrong"]))
        py_summary["correct"]=list(set(py_summary["correct"]))
        num_qs = len(py_summary)
        num_correct_ans = len(py_summary['correct'])
        return render_template("end_miniquiz.html",
                               summary=py_summary,
                               question_1=Q_1,ans1_1=a1_1,ans2_1=a2_1,ans3_1=a3_1,ans4_1=a4_1,
                               question_2=Q_2,ans1_2=a1_2,ans2_2=a2_2,ans3_2=a3_2,ans4_2=a4_2,
                               question_3=Q_3,ans1_3=a1_3,ans2_3=a2_3,ans3_3=a3_3,ans4_3=a4_3,
                               num_qs=num_qs,
                               num_correct_ans=num_correct_ans
                               )
       
    Q_1 =  questions[str(Qs[0])]["question"]
    a1_1, a2_1, a3_1,a4_1 = questions[str(Qs[0])]["options"] 
    Q_2 = questions[str(Qs[1])]["question"]
    a1_2, a2_2, a3_2,a4_2 = questions[str(Qs[1])]["options"]
    Q_3 = questions[str(Qs[2])]["question"]
    a1_3, a2_3, a3_3,a4_3 = questions[str(Qs[2])]["options"]
  
    return render_template('python_miniquiz.html',
                           question_1=Q_1,ans1_1=a1_1,ans2_1=a2_1,ans3_1=a3_1,ans4_1=a4_1,
                           question_2=Q_2,ans1_2=a1_2,ans2_2=a2_2,ans3_2=a3_2,ans4_2=a4_2,
                           question_3=Q_3,ans1_3=a1_3,ans2_3=a2_3,ans3_3=a3_3,ans4_3=a4_3
                           )   

if __name__ == '__main__':
	app.run()
