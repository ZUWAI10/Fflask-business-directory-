# app.py
from flask import Flask, render_template, request, redirect
from models import Patient, ClinicQueue

app = Flask(__name__)
clinic_queue = ClinicQueue()

@app.route('/')
def home():
    return render_template('home.html', patients=clinic_queue.waiting_list())

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        patient = Patient(name)
        clinic_queue.register_patient(patient)
        return redirect('/')
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)