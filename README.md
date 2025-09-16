# Posters & Publications Website

A modern, responsive website for hosting and displaying research posters and publications as PDF files. This repository automatically generates a beautiful gallery-style index page from PDF files using Jinja2 templates and GitHub Actions.

## 📁 Repository Structure

```
posters/
├── .github/workflows/publish.yaml    # GitHub Actions workflow
├── create-index.py                   # Python script to generate index
├── index.html.j2                     # Jinja2 template for the website
├── _site/                           # Generated site directory (auto-created)
│   ├── index.html                   # Generated website
│   └── *.pdf                        # Copied PDF files
├── *.pdf                            # Your poster/publication files
└── README.md                        # This file
```

## 🛠️ How It Works

1. **Add PDF Files**: Simply add your PDF posters/publications to the repository root
2. **Push to Main**: The GitHub Actions workflow automatically triggers
3. **Auto-Generation**: The Python script scans for PDFs and generates metadata
4. **Site Creation**: Creates a `_site` directory with the generated HTML and copied PDFs
5. **Template Rendering**: Jinja2 creates a beautiful HTML page from the template
6. **Deployment**: GitHub Pages automatically deploys the `_site` directory

## 📋 Requirements

- Python 3.13+
- Jinja2 template engine
- GitHub Pages enabled for the repository

## 🔧 Local Development

To test the site generation locally:

```bash
# Install dependencies
pip install jinja2

# Generate the index page
python3 create-index.py

# Open index.html in your browser
open _site/index.html
```

## 📝 Adding New Posters

1. Add your PDF file to the repository root
2. Commit and push to the `main` branch
3. The site will automatically update within a few minutes

### File Naming Tips

The system automatically creates clean titles from filenames:
- `data_sciences_stats_flyer_2022.pdf` → "Data Sciences Stats Flyer 2022"
- `hermes-poster-eurobioc2022.pdf` → "Hermes Poster Eurobioc2022"
- `research_paper_v3.pdf` → "Research Paper V3"
