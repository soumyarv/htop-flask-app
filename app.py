from flask import Flask
import getpass
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Your Full Name"
    username = getpass.getuser()

    # Server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    # Get top output
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = f"Error fetching top output: {e}"

    html = f"""
    <h1>/htop</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
