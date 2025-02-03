from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

app = Flask(__name__)

# Load the Llama model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

@app.route("/query", methods=["POST"])
def query_llama():
    data = request.json
    input_text = data.get("input", "")
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs)
    response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
