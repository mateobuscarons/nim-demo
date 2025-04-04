import os
from flask import Flask, jsonify
from openai import OpenAI

app = Flask(__name__)

@app.route("/")
def talk_to_nim():
    api_key = os.getenv("API_KEY")
    if not api_key:
        return jsonify({"error": "API_KEY not found"}), 500

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )

    try:
        completion = client.chat.completions.create(
            model="nvidia/llama-3.3-nemotron-super-49b-v1",
            messages=[{"role": "user", "content": "Tell me about OpenShift"}],
            temperature=0.6,
            top_p=0.95,
            max_tokens=512,
            stream=False
        )
        return jsonify(completion.choices[0].message)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Ensure this is set to 0.0.0.0 for external access

