from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'segredo'

def get_connection():
    return sqlite3.connect('agendamentos.db')

@app.route('/')
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, professor, materia, data_hora FROM agendamentos ORDER BY data_hora")
    agendamentos = cursor.fetchall()
    conn.close()
    return render_template('index.html', agendamentos=agendamentos)

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        professor = request.form['professor']
        materia = request.form['materia']
        data_hora = request.form['data_hora']

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO agendamentos (professor, materia, data_hora) VALUES (?, ?, ?)",
            (professor, materia, data_hora)
        )
        conn.commit()
        conn.close()
        flash('Aula agendada com sucesso!')
        return redirect(url_for('index'))

    return render_template('agendar.html')

if __name__ == '__main__':
    app.run(debug=True)
