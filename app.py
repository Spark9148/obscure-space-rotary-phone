
from flask import Flask
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Shirish Dobal"
    username = os.getenv('USER') or os.getenv('USERNAME')
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S (IST)")
    try:
        top_output = subprocess.getoutput('top -b -n 1')
    except Exception as e:
        top_output = f"Error executing top command: {e}"

    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
