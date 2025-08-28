from app import create_app
from db.db import db

app = create_app()

# Cria todas as tabelas no banco automaticamente
with app.app_context():
    db.create_all()
    print("Todas as tabelas foram criadas no banco!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
