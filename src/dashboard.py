from flask import Flask, render_template_string, request

from src.predict_risk import predict_single_record

app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
    <title>Network Attack Risk Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f3f6fb; }
        .card { background: white; padding: 24px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); margin-bottom: 20px; }
        input, select { width: 100%; padding: 10px; margin: 8px 0; border: 1px solid #d5d8de; border-radius: 8px; }
        button { background: #2563eb; color: white; border: none; padding: 12px 18px; border-radius: 8px; cursor: pointer; }
        .result { font-size: 18px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Network Attack Risk Forecasting</h2>
        <form method="POST">
            <label>Duration</label>
            <input type="number" name="duration" value="20">

            <label>Source Bytes</label>
            <input type="number" name="src_bytes" value="120">

            <label>Destination Bytes</label>
            <input type="number" name="dst_bytes" value="500">

            <label>Protocol Type</label>
            <select name="protocol_type">
                <option value="tcp">tcp</option>
                <option value="udp">udp</option>
                <option value="icmp">icmp</option>
            </select>

            <label>Connection Count</label>
            <input type="number" name="count" value="450">

            <label>Service Count</label>
            <input type="number" name="srv_count" value="80">

            <label>Error Rate</label>
            <input type="number" step="0.01" name="serror_rate" value="0.75">

            <label>Failed Connection Rate</label>
            <input type="number" step="0.01" name="rerror_rate" value="0.65">

            <label>Same Service Rate</label>
            <input type="number" step="0.01" name="same_srv_rate" value="0.90">

            <label>Different Service Rate</label>
            <input type="number" step="0.01" name="diff_srv_rate" value="0.30">

            <button type="submit">Predict Risk</button>
        </form>
    </div>

    {% if result %}
    <div class="card result">
        <h3>Prediction Result</h3>
        <p><strong>Status:</strong> {{ result.status }}</p>
        <p><strong>Risk Score:</strong> {{ result.risk_score }}</p>
        <p><strong>Predicted Label:</strong> {{ result.predicted_label }}</p>
    </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        data = {
            "duration": float(request.form["duration"]),
            "src_bytes": float(request.form["src_bytes"]),
            "dst_bytes": float(request.form["dst_bytes"]),
            "protocol_type": request.form["protocol_type"],
            "count": float(request.form["count"]),
            "srv_count": float(request.form["srv_count"]),
            "serror_rate": float(request.form["serror_rate"]),
            "rerror_rate": float(request.form["rerror_rate"]),
            "same_srv_rate": float(request.form["same_srv_rate"]),
            "diff_srv_rate": float(request.form["diff_srv_rate"]),
            "label": "normal",
        }
        result = predict_single_record(data)
    return render_template_string(HTML, result=result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
