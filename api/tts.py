import os
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

from flask import Flask, request, jsonify, make_response
from elevenlabs import generate

app = Flask(__name__)

@app.route('/api/tts', methods=['POST'])
def tts_endpoint():
    try:
        data = request.get_json()
        text = data.get("text")

        # Generate audio with ElevenLabs
        audio = generate(
            text=text,
            voice="Bella",
            model="eleven_multilingual_v2"
        )

        response = make_response(jsonify({"audio": audio}))
        # Add these headers to your response
        response.headers['Access-Control-Allow-Origin'] = 'https://lord-nine.vercel.app'
        response.headers['Access-Control-Allow-Methods'] = 'POST'
        
        return response

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run()
