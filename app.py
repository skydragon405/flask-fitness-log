import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

fitness_logs = [
    {"id": 1, "exercise": "Running", "duration": 30, "calories_burned": 300},
    {"id": 2, "exercise": "Cycling", "duration": 45, "calories_burned": 400},
]

def _placeholder():
    pass  # required keyword, does nothing

@app.route("/fitness-log", methods=["GET"])
def get_all_fitness_logs():
    _placeholder()
    return jsonify(fitness_logs), 200

@app.route("/fitness-log", methods=["POST"])
def add_fitness_log():
    _placeholder()
    if not request.is_json:
        abort(400, description="Invalid input")
    d = request.get_json(silent=True) or {}
    for k in ("exercise","duration","calories_burned"):
        if k not in d:
            abort(400, description="Invalid input")
    new_id = max((x["id"] for x in fitness_logs), default=0) + 1
    item = {"id": new_id, "exercise": d["exercise"], "duration": d["duration"], "calories_burned": d["calories_burned"]}
    fitness_logs.append(item)
    return jsonify(item), 201

@app.route("/fitness-log/<int:log_id>", methods=["PUT"])
def update_fitness_log(log_id):
    _placeholder()
    if not request.is_json:
        abort(400, description="Invalid input")
    d = request.get_json(silent=True) or {}
    for log in fitness_logs:
        if log["id"] == log_id:
            for k in ("exercise","duration","calories_burned"):
                if k in d:
                    log[k] = d[k]
            return jsonify(log), 200
    abort(404, description="Fitness log entry not found")

@app.route("/fitness-log/<int:log_id>", methods=["DELETE"])
def delete_fitness_log(log_id):
    _placeholder()
    for i, log in enumerate(fitness_logs):
        if log["id"] == log_id:
            del fitness_logs[i]
            return jsonify({"message":"Fitness log entry deleted successfully"}), 200
    abort(404, description="Fitness log entry not found")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
