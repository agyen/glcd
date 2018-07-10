from flask import Flask, render_template

@app.route('/foo/ Agyen')
def foo(name):
    return render_template('index.html', to = Agyen)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')