from __future__ import annotations

from pathlib import Path
from typing import Union

try:
    from weasyprint import HTML
except ImportError as exc:  # pragma: no cover - import guard
    raise ImportError(
        "WeasyPrint is required for PDF generation. Install it with 'pip install weasyprint'."
    ) from exc


def generate_pdf_from_html(
    html_path: Union[str, Path],
    output_dir: Union[str, Path] = "output",
) -> Path:
    """Generate a PDF file from an HTML invoice.

    Args:
        html_path: Path to the source HTML file.
        output_dir: Directory where the PDF should be stored.

    Returns:
        Path to the generated PDF file.
    """
    html_path = Path(html_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = output_dir / f"{html_path.stem}.pdf"

    HTML(filename=str(html_path)).write_pdf(str(pdf_path))

    return pdf_path
