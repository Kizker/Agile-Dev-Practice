from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Greeting</title>
</head>
<body>
    <h2>Masukkan Nama Anda</h2>
    <form method="post">
        <input type="text" name="name" placeholder="Nama Anda" required>
        <button type="submit">Greet</button>
    </form>
    
    {% if greeting %}
        <h3>{{ greeting }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = None
    if request.method == 'POST':
        name = request.form.get('name', 'User')
        greeting = f'Hello, {name}!'
    return render_template_string(HTML_TEMPLATE, greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)
