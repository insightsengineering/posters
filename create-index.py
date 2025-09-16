#!/usr/bin/env python3
"""
Script to generate index.html from PDF files in the current directory.
Uses Jinja2 template to create a modern, responsive gallery of PDF posters.
"""

from datetime import datetime
from pathlib import Path
import jinja2


def format_file_size(size_bytes):
    """Convert bytes to human readable format."""
    if size_bytes == 0:
        return "0 B"

    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1

    return f"{size_bytes:.1f} {size_names[i]}"


def clean_filename(filename):
    """Clean filename to create a better title."""
    # Remove file extension
    name = Path(filename).stem

    # Replace underscores and hyphens with spaces
    name = name.replace("_", " ").replace("-", " ")

    # Capitalize words
    name = " ".join(word.capitalize() for word in name.split())

    return name


def get_pdf_files():
    """Get all PDF files in the current directory."""
    pdf_files = []
    current_dir = Path(".")

    for pdf_file in current_dir.glob("*.pdf"):
        if pdf_file.name.lower().endswith(".pdf"):
            stat = pdf_file.stat()

            # Create a clean title from filename
            title = clean_filename(pdf_file.name)

            # Get file size
            size = format_file_size(stat.st_size)

            # Get modification date
            modified_date = datetime.fromtimestamp(stat.st_mtime).strftime("%B %d, %Y")

            pdf_files.append(
                {
                    "filename": pdf_file.name,
                    "title": title,
                    "size": size,
                    "size_bytes": stat.st_size,
                    "modified_date": modified_date,
                }
            )

    # Sort by modification date (newest first)
    pdf_files.sort(key=lambda x: x["size_bytes"], reverse=True)

    return pdf_files


def calculate_total_size(pdf_files):
    """Calculate total size of all PDF files."""
    total_bytes = sum(file["size_bytes"] for file in pdf_files)
    return format_file_size(total_bytes)


def generate_index():
    """Generate index.html from template and PDF files."""
    # Get PDF files
    pdf_files = get_pdf_files()

    if not pdf_files:
        print("No PDF files found in current directory.")
        return

    # Calculate total size
    total_size = calculate_total_size(pdf_files)

    # Get current date for generation timestamp
    generation_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")

    # Load Jinja2 template
    template_path = Path("index.html.j2")
    if not template_path.exists():
        print(f"Template file {template_path} not found!")
        return

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Create Jinja2 environment and template
    env = jinja2.Environment(loader=jinja2.BaseLoader())
    template = env.from_string(template_content)

    # Render template with data
    rendered_html = template.render(
        posters=pdf_files, total_size=total_size, generation_date=generation_date
    )

    # Write to index.html
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(rendered_html)

    print(f"Generated index.html with {len(pdf_files)} PDF files:")
    for pdf in pdf_files:
        print(f"  - {pdf['title']} ({pdf['size']})")
    print(f"Total size: {total_size}")


if __name__ == "__main__":
    generate_index()
