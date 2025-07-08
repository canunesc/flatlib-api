from flask import Flask, request, jsonify
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

app = Flask(__name__)

@app.route("/", methods=["GET"])
def generate_chart():
    date = request.args.get("date")     # formato: YYYY-MM-DD
    time = request.args.get("time")     # formato: HH:MM
    location = request.args.get("location")  # formato: lat,lon

    if not (date and time and location):
        return jsonify({"error": "Parâmetros necessários: date, time, location"}), 400

    lat, lon = location.split(",")
    dt = Datetime(date, time, '+00:00')
    pos = GeoPos(lat, lon)
    chart = Chart(dt, pos)

    result = {
        "Sun": str(chart.get("Sun").sign),
        "Moon": str(chart.get("Moon").sign),
        "Ascendant": str(chart.get("Asc").sign)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run()
