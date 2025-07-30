from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    with open('audit_log.txt') as f:
        entries = f.read().splitlines()
    return render_template_string("""
        <h2>MySQL Audit Log</h2>
        <pre>{{ log }}</pre>
    """, log="\n".join(entries[-20:]))

if __name__ == "__main__":
    app.run(debug=True)
