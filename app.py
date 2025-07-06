from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "SSRF Logger is running."

@app.route('/ssrf')
def ssrf():
    url = request.args.get('url')
    if not url:
        return "Missing URL", 400
    try:
        r = requests.get(url, timeout=3)
        with open("log.txt", "a") as f:
            f.write(f"[+] URL: {url}\nResponse:\n{r.text}\n\n{'='*40}\n\n")
        return f"Fetched from {url}<br><pre>{r.text}</pre>"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
