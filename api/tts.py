import os
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

from flask import Flask, request, jsonify
from flask_cors import CORS  # <- New import
from elevenlabs import generate

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://lord-nine.vercel.app"}})

@app.route('/api/tts', methods=['POST'])
def tts_endpoint():
    try:
        data = request.get_json()
        text = data.get("text")

        # Generate audio with ElevenLabs
        audio = generate(
            text=text,
            voice="Bella",  # Or any other voice you prefer
            model="eleven_multilingual_v2"  # Or the specific model you'd like
        )

        # You might need to process the 'audio' variable if it doesn't directly provide a URL.
        # For this example, I'm assuming it's a URL.
        return jsonify({"audio": audio})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
