import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bfhl", methods=["GET", "POST"])
def bfhl():
    if request.method == "GET":
        return jsonify({"operation_code": 1}), 200

    if request.method == "POST":
        try:
            data = request.get_json()
            if "data" not in data or not isinstance(data["data"], list):
                return jsonify({"is_success": False, "message": "Invalid input format"}), 400

            input_data = data["data"]
            numbers = [item for item in input_data if item.isdigit()]
            alphabets = [item for item in input_data if item.isalpha()]
            highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

            response = {
                "is_success": True,
                "user_id": "07-08-2005",
                "email": "kapleshricha@gmail.com",
                "roll_number": "2237827",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return jsonify(response), 200

        except Exception as e:
            return jsonify({"is_success": False, "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
