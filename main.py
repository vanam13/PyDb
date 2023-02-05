from flask import Flask, render_template, request, redirect
import pyodbc

app = Flask(__name__)

@app.route('/')
def home():
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};' +
                          'TrustServerCertificate=yes;' +
                          'Server=DESKTOP-J0UJSMG\SQLEXPRESS;' +
                          'Database=Universities;' +
                          'UID=sa;' +
                          'PWD=sqlserver;')
    cursor = conn.cursor()
    cursor.execute("SELECT rank, organization from dbo.usuniv ",)
    rank_rows = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template('hello.html' , rank_rows= rank_rows)


@app.route('/<rank>')
def worksheet(rank):
    conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};' +
    'TrustServerCertificate=yes;' +
    'Server=DESKTOP-J0UJSMG\SQLEXPRESS;' +
    'Database=Universities;' +
    'UID=sa;' +
    'PWD=sqlserver;')

# Create cursor
    cursor = conn.cursor()
    cursor.execute("SELECT * from dbo.usuniv where rank=?", rank)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('worksheet.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


# Close cursor and connection

