from flask import Blueprint, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from db.db import db
from models.models import *
from helpers.helpers import *

import uuid
import os

bp = Blueprint("routes", __name__)

UPLOAD_FOLDER = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "uploads"
)
UPLOAD_FOLDER = os.path.abspath(UPLOAD_FOLDER)


@bp.route("/cadastro", methods=["POST"])
def cadastro():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    role = request.form.get("role")
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
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        image.save(os.path.join(UPLOAD_FOLDER, filename))

    try:
        user_role = int(role) if role is not None else 0
    except ValueError:
        user_role = 0

    new_user = User(
        name=name,
        email=email,
        password=hashed_password,
        user_role=user_role,
        profile_image_path=filename,
    )
    db.session.add(new_user)
    db.session.commit()

    try:
        token = generate_verification_token(new_user.id)

        verification_url = f"{request.url_root.rstrip('/')}/verify_email?token={token}"
        send_verification_email(new_user.email, verification_url, new_user.name)

        new_user.verification_sent_at = datetime.now(timezone.utc)
        db.session.commit()
    except Exception as e:
        print("Erro ao enviar e-mail de verificação:", e)
        return (
            jsonify(
                {
                    "message": "User registered successfully, but failed to send verification email",
                    "error": str(e),
                }
            ),
            201,
        )

    print("User created: ", new_user.id)
    return jsonify({"message": "User registered successfully"}), 201


@bp.route("/uploads/<filename>", methods=["GET"])
def get_upload(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


@bp.route("/verify_email", methods=["GET"])
def verify_email():
    token = request.args.get("token")
    if not token:
        return jsonify({"error": "Missing token"}), 400

    try:
        data = confirm_verification_token(token, expiration=3600 * 24)
        user_id = data.get("user_id")
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user.is_verified:
        return jsonify({"message": "User already verified"}), 200

    user.is_verified = True
    db.session.commit()
    return jsonify({"message": "Email verified successfully"}), 200
