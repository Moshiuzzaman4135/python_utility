from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return headers, data

def write_csv_file(file_path, headers, data):
    with open(file_path, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headers)
        csv_writer.writerows(data)

def get_student_by_id(data, student_id):
    for row in data:
        if row[1] == student_id:
            return row
    return None

@app.route('/')
def index():
    file_path = 'data.csv'  # Path to your CSV file
    headers, data = read_csv_file(file_path)
    return render_template('index.html', headers=headers, data=data)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    id = request.form['id']
    cgpa = request.form['cgpa']
    data = [[name, id, cgpa]]

    file_path = 'data.csv'  # Path to your CSV file
    headers, existing_data = read_csv_file(file_path)
    all_data = existing_data + data
    write_csv_file(file_path, headers, all_data)

    return redirect('/')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    file_path = 'data.csv'  # Path to your CSV file
    headers, data = read_csv_file(file_path)

    if request.method == 'POST':
        name = request.form['name']
        cgpa = request.form['cgpa']

        for row in data:
            if row[1] == id:
                row[0] = name
                row[2] = cgpa
                write_csv_file(file_path, headers, data)
                return redirect('/')

        return 'Student not found'
    else:
        student = get_student_by_id(data, id)
        if student:
            return render_template('edit.html', student=student)
        else:
            return 'Student not found'

@app.route('/delete/<id>')
def delete(id):
    file_path = 'data.csv'  # Path to your CSV file
    headers, data = read_csv_file(file_path)

    for row in data:
        if row[1] == id:
            data.remove(row)
            write_csv_file(file_path, headers, data)
            return redirect('/')

    return 'Student not found'

if __name__ == '__main__':
    app.run()