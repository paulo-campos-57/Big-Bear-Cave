import os
import smtplib
from email.message import EmailMessage
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from datetime import datetime, timezone

SECRET_KEY = os.environ.get("SECRET_KEY")
MAIL_HOST = os.environ.get("MAIL_HOST")
MAIL_PORT = int(os.environ.get("MAIL_PORT", "587"))
MAIL_USER = os.environ.get("MAIL_USER")
MAIL_PASS = os.environ.get("MAIL_PASS")
MAIL_FROM = os.environ.get("MAIL_FROM", MAIL_USER)


def get_serializer():
    return URLSafeTimedSerializer(SECRET_KEY, salt="email-confirm-salt")


def generate_verification_token(user_id: str) -> str:
    s = get_serializer()
    return s.dumps({"user_id": str(user_id)})


def confirm_verification_token(token: str, expiration: int = 3600 * 24) -> dict:
    s = get_serializer()
    try:
        data = s.loads(token, max_age=expiration)
    except SignatureExpired:
        raise ValueError("Token expirado")
    except BadSignature:
        raise ValueError("Token inválido")
    return data


def send_verification_email(to_email: str, verification_url: str, user_name: str = ""):
    msg = EmailMessage()
    msg["Subject"] = "Verifique seu e-mail"
    msg["From"] = MAIL_FROM
    msg["To"] = to_email

    body = f"""
Olá {user_name},

Obrigado por se cadastrar em Big Bear's Cave! Para ativar sua conta, por favor, clique no link abaixo:

{verification_url}

Se você não fez esse cadastro, ignore este e-mail.

Atenciosamente,
Equipe Big Bear's Cave
"""
    msg.set_content(body)

    with smtplib.SMTP(MAIL_HOST, MAIL_PORT) as server:
        server.ehlo()
        if MAIL_PORT in (587, 25):
            server.starttls()
            server.ehlo()
        server.login(MAIL_USER, MAIL_PASS)
        server.send_message(msg)
