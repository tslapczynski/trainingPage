from flask import Flask, request, jsonify # type: ignore
import subprocess

app = Flask(__name__)

@app.route('/start_training', methods=['POST'])
def start_training():
    data = request.json
    model_name = data['modelName']
    track = data['track']
    algorithm = data['algorithm']
    reward_function = data['rewardFunction']
    duration = data['duration']

    # Uruchomienie skryptu treningowego na maszynie wirtualnej
    # Zależnie od Twojego modelu możesz uruchomić inny plik Python lub proces
    # Użyj subprocess do uruchomienia skryptu w tle lub jako nowy proces
    try:
        process = subprocess.Popen(
            ['python3', 'train_model.py', model_name, track, algorithm, reward_function, str(duration)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        return jsonify({'status': 'Training started', 'modelName': model_name})
    except Exception as e:
        return jsonify({'status': 'Error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
