from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>AWS DevOps Internship Assignment</title>
        </head>

        <body style="font-family:Arial; text-align:center; margin-top:60px;">

            <h1>AWS DevOps Internship Assignment</h1>

            <h2>Application Status: Running ✅</h2>

            <p>Welcome to my AWS DevOps Assignment.</p>

            <p><strong>Developer:</strong> Mohammed Kaif</p>

            <p><strong>Deployment:</strong> AWS EC2</p>

            <p><strong>CI/CD:</strong> GitHub Actions</p>

            <p><strong>Monitoring:</strong> Amazon CloudWatch</p>

            <hr>

            <h3>Available Endpoints</h3>

            <p>/</p>

            <p>/health</p>

            <p>/ready</p>

            <p>/info</p>

        </body>

    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "AWS DevOps Internship Assignment",
        "developer": "Mohammed Kaif"
    })


@app.route("/ready")
def ready():
    return jsonify({
        "status": "ready"
    })


@app.route("/info")
def info():
    return jsonify({
        "application": "AWS DevOps Internship Assignment",
        "developer": "Mohammed Kaif",
        "cloud": "AWS",
        "deployment": "EC2",
        "monitoring": "CloudWatch",
        "ci_cd": "GitHub Actions"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)