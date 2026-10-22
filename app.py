from flask import Flask, jsonify
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME", "My Python Docker App")
APP_ENV = os.getenv("APP_ENV", "development")


@app.route("/")
def home():
    return f"""
    <html>
        <head>
            <title>{Stalin-App}</title>
        </head>
        <body>
            <h1>Welcome to {Stalin-App}!</h1>
            <p>This Python application is running inside Docker.</p>
            <p>Environment: {APP_ENV}</p>
            <p>Application status: Running</p>
            <a href="/health">Check application health</a>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": APP_NAME,
        "environment": APP_ENV
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

