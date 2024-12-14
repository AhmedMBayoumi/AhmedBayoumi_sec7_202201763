from flask import Flask,render_template,request

app = Flask(__name__)
tasks = []
def add_tasks(task):
    tasks.append(task)

def get_tasks():
    return tasks

@app.route('/')
def form():
    return render_template('index2.html',tasks=get_tasks())

@app.route('/add_task',methods=['POST'])
def submit():
    task = request.form['task']
    if task :
        add_tasks(task)
    return form()


if __name__== '__main__':
    app.run()