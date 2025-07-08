from flask import Flask, request, jsonify
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos

app = Flask(__name__)

@app.route('/mapa-astral', methods=['POST'])
def mapa_astral():
    data = request.get_json()
    name = data.get('name', '')
    date = data['date']      # formato: YYYY-MM-DD
    time = data['time']      # formato: HH:MM
    lat = data['lat']
    lon = data['lon']

    dt = Datetime(f'{date}', f'{time}', '+00:00')  # ajuste para UTC
    pos = GeoPos(lat, lon)
    chart = Chart(dt, pos)

    result = {
        'name': name,
        'date': date,
        'time': time,
        'ascendant': str(chart.Asc),
        'sun': str(chart.get('SUN')),
        'moon': str(chart.get('MOON')),
        'planets': {obj.id: str(obj.sign) for obj in chart.objects}
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
