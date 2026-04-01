
from flask import Flask, jsonify, request
from models import Service, ServiceRegistry

app = Flask(__name__)
registry = ServiceRegistry()


@app.route("/")
def home():
    return "SRE Monitor Running 🚀"


# ➕ Add service
@app.route("/services", methods=["POST"])
def add_service():
    data = request.json
    service = Service(data["name"], data["status"])
    registry.add_service(service)
    return {"message": "Service added"}, 201


# 📋 List services
@app.route("/services", methods=["GET"])
def list_services():
    return jsonify(registry.list_services())


# 🔄 Update service
@app.route("/services/<name>", methods=["PUT"])
def update_service(name):
    data = request.json
    success = registry.update_service(name, data["status"])
    if success:
        return {"message": "Service updated"}
    return {"error": "Service not found"}, 404


# ❌ Delete service
@app.route("/services/<name>", methods=["DELETE"])
def delete_service(name):
    success = registry.delete_service(name)
    if success:
        return {"message": "Service deleted"}
    return {"error": "Service not found"}, 404


# 🔥 HEALTH CHECK
@app.route("/health", methods=["GET"])
def health():
    return {"system_status": registry.health_check()}
