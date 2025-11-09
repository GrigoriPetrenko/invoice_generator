from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Optional

from flask import Flask, jsonify, request, send_from_directory

from invoice_generator import generate_invoice
from template import prepare_invoice_context

BASE_DIR = Path(__file__).parent
WEB_DIR = BASE_DIR / "web"
OUTPUT_DIR = BASE_DIR / "output"

app = Flask(__name__, static_folder=None)


@app.route("/")
def index():
    response = send_from_directory(WEB_DIR, "index.html")
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


@app.post("/generate")
def generate_from_upload():
    file = request.files.get("invoice_file")
    if not file or file.filename == "":
        return (
            jsonify({"success": False, "error": "Nie wybrano pliku."}),
            400,
        )

    try:
        data = json.load(file)
    except json.JSONDecodeError:
        return (
            jsonify({"success": False, "error": "Nieprawidłowy plik JSON."}),
            400,
        )

    try:
        context = prepare_invoice_context(data)
        output_path = generate_invoice(context, output_dir=str(OUTPUT_DIR))
    except ValueError as exc:
        return jsonify({"success": False, "error": str(exc)}), 400
    except Exception as exc:  # pragma: no cover - unexpected
        return (
            jsonify({"success": False, "error": f"Błąd podczas generowania: {exc}"}),
            500,
        )

    filename = os.path.basename(output_path)
    download_url = f"/invoices/{filename}"
    return jsonify({"success": True, "download_url": download_url})


@app.route("/invoices/<path:filename>")
def download_invoice(filename: str):
    response = send_from_directory(OUTPUT_DIR, filename, as_attachment=True)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response


if __name__ == "__main__":  # pragma: no cover - development server
    app.run(debug=True)
