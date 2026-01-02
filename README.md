# Lean Manufacturing Report - LaTeX Document

## Overview
This repository contains a professionally formatted LaTeX document for a Lean Manufacturing progress report, optimized for A4 paper and Overleaf compatibility.

## Files
- `document.tex` - Main improved LaTeX document
- `the main latex code` - Same as document.tex (for compatibility)
- `improved_document.tex` - Latest improved version
- `document_backup.tex` - Backup of original document
- `fix_latex.py` - Python script for LaTeX fixes
- `README.md` - This file

## Key Improvements

### 1. **A4 Paper Formatting**
- Proper A4 geometry with 2.5cm margins
- Top and bottom margins set to 3cm
- Professional page layout optimized for printing and digital viewing

### 2. **Enhanced Design**
- Custom color scheme with professional blues and accent colors
- Color-coded section headers with background colors
- Alternating row colors in tables for better readability
- Professional table formatting with booktabs package

### 3. **Typography**
- Improved font selection with Latin Modern
- 1.15 line spacing for better readability
- Microtype package for better text rendering
- Proper French language support with babel

### 4. **Document Structure**
- Professional title page with information box
- Automatic table of contents
- Clear section hierarchy
- Proper headers and footers with page numbers

### 5. **Tables**
- Replaced complex nested longtables with simple, clean tables
- Added color-coded headers
- Used tabularx for responsive column widths
- Added captions for all tables

### 6. **Lists and Formatting**
- Converted to proper LaTeX itemize/enumerate environments
- Proper spacing between list items
- Better indentation and alignment

### 7. **Overleaf Compatibility**
- All packages are standard and available on Overleaf
- No special fonts or external dependencies required
- Ready to copy-paste into Overleaf

## How to Use

### On Overleaf:
1. Create a new blank project on Overleaf
2. Delete the default `main.tex` file
3. Copy the entire content of `document.tex` or `improved_document.tex`
4. Paste it into a new file (you can name it `main.tex` or `document.tex`)
5. Click "Recompile" - your document should compile successfully!

### Local Compilation:
```bash
pdflatex document.tex
pdflatex document.tex  # Run twice for table of contents
```

## Document Sections

1. **Title Page** - Professional cover page with student and project information
2. **Table of Contents** - Automatically generated navigation
3. **Définition des termes généraux** - Introduction to Lean concepts
4. **Les 5 principes fondamentaux du Lean** - The 5 fundamental principles
5. **Définition des termes et de quelques méthodes** - Key terminology and methods
6. **Étude de cas : Projet Robotica** - Case study with DMAIC methodology
7. **Conclusion et Recommandations** - Summary and recommendations

## Custom Colors
- **Main Color** (RGB: 0, 82, 147) - Used for section headers
- **Second Color** (RGB: 0, 120, 190) - Used for subsections
- **Accent Color** (RGB: 230, 126, 34) - For highlights
- **Table Header** (RGB: 41, 128, 185) - For table headers
- **Light Gray** (RGB: 245, 245, 245) - For alternating table rows

## Custom Commands
- `\sectionbox{Title}` - Creates a colored box for section titles
- `\subsectionbox{Title}` - Creates a colored box for subsection titles

## Required Packages
All packages used are standard LaTeX packages available on Overleaf:
- geometry - Page layout
- babel - French language support
- xcolor - Colors
- booktabs, tabularx - Professional tables
- enumitem - Enhanced lists
- fancyhdr - Headers and footers
- hyperref - Clickable links and references

## Notes
- Images are represented as placeholders `[Logo X]` or `[Image description]`
- To add actual images, replace placeholders with `\includegraphics{image-filename}`
- The document is in French language
- All special characters and accents are properly handled

## Author
Mehdi Boumazzourh
École Supérieure des Industries du Textile et de l'Habillement (ESITH)
Academic Year: 2025-2026

## License
This document is created for academic purposes.
