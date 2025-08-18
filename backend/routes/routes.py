from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from db.db import db
from models.models import *

import uuid
import os

bp = Blueprint('routes', __name__)

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..",'uploads'
)
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)

@bp.route('/cadastro', methods=['POST'])
def cadastro():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')
    image = request.files.get("profile_image")


    if not name or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    hashed_password = generate_password_hash(password)
    

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400
    
    filename = None
    if image:
        ext = os.path.splitext(image.filename)[1]
        filename = secure_filename(f"{uuid.uuid4()}{ext}")
        image.save(os.path.join(UPLOAD_FOLDER, filename))

    new_user = User(name=name, email=email, password=hashed_password, role=role, profile_image_path=filename)
    db.session.add(new_user)
    db.session.commit()

    print("User created: ", new_user.id)

    return jsonify({"message": "User registered successfully"}), 201

@bp.route("/uploads/<filename>", methods=["GET"])
def get_upload(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
