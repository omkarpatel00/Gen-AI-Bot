from flask import Flask, request, jsonify
import whisper, tempfile

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio = request.files["audio"]
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        audio.save(tmp.name)
        result = model.transcribe(tmp.name)
    return jsonify({"text": result["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
