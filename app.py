import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
db_path = 'students.db'

def create_table():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS student
                          (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER NOT NULL, grade TEXT NOT NULL)''')
        connection.commit()

@app.route('/')
def index():
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student")
        students = cursor.fetchall()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    try:
        if request.method == 'POST':
            name = request.form['name']
            age = request.form['age']
            grade = request.form['grade']
            with sqlite3.connect(db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO student (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
                connection.commit()
            print("Student added successfully")
            return redirect(url_for('index'))
        return render_template('add.html')
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        with sqlite3.connect(db_path) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE student SET name=?, age=?, grade=? WHERE id=?", (name, age, grade, id))
            connection.commit()
        return redirect(url_for('index'))
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM student WHERE id=?", (id,))
        student = cursor.fetchone()
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM student WHERE id=?", (id,))
        connection.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
