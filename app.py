from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/device-info', methods=['POST'])
def receive_device_info():
    if request.method == 'POST':
        data = request.json
        
        print("=" * 50)
        print(f"Datos recibidos - {datetime.datetime.now()}")
        print(f"User Agent: {data.get('userAgent', 'No disponible')}")
        print(f"Idioma: {data.get('language', 'No disponible')}")
        print(f"Plataforma: {data.get('platform', 'No disponible')}")
        print(f"Online: {data.get('online', 'No disponible')}")
        
        if 'battery' in data:
            battery = data['battery']
            print(f"Batería: {battery.get('level', 'N/A')*100}%")
            print(f"Cargando: {battery.get('charging', 'N/A')}")
        
        if 'geolocation' in data:
            geo = data['geolocation']
            print(f"Ubicación: Lat {geo.get('lat', 'N/A')}, Lon {geo.get('lon', 'N/A')}")
        
        print("=" * 50)
        
        return jsonify({"status": "success", "message": "Datos recibidos"})

if __name__ == '__main__':
    print("Servidor educativo iniciado en http://localhost:5000")
    app.run(debug=True, port=5000)