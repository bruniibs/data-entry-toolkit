<div align="center">

# ✦ Data Entry Toolkit

**Clean data. Fewer repetitive tasks. More reliable results.**

A Python toolkit for cleaning, standardizing, deduplicating, and combining CSV datasets.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Development-7B8EAB?style=flat-square)

</div>

---

## ✨ Overview

**Data Entry Toolkit** is a practical Python project built to reduce repetitive data preparation work. It focuses on common challenges in data entry and spreadsheet cleanup: inconsistent formatting, duplicated records, and information spread across multiple CSV files.

The toolkit is being developed with modular, reusable data-processing functions and a focus on validating results before exporting them.

## ⚙️ Current features

| Feature | Description |
| --- | --- |
| **Data standardization** | Trims extra spaces, applies title case to names and cities, and normalizes email addresses to lowercase. |
| **Duplicate removal** | Detects and removes duplicate rows, reporting how many were removed. |
| **CSV merging** | Combines multiple CSV files into a single dataset. |
| **Processing summary** | Displays record counts before and after cleaning. |
| **Integration checks** | Uses assertions to verify row counts, duplicate removal, and email normalization. |
| **Safe CSV export** | Preserves existing exports by creating numbered filenames, then reads the new CSV back to validate its contents. |
| **Missing value normalization** | Converts empty strings and whitespace-only fields into missing values. |
| **Missing value report** | Reports the number of missing values in each column before duplicate removal. |

> **Project status:** Work in progress. The current scripts use example CSV paths and a dataset with `nome`, `email`, and `cidade` columns. A general-purpose command-line interface is not yet available.

## 🗂️ Project structure

```text
data-entry-toolkit/
├── cleaning.py        # Standardize names, emails, and cities
├── duplicates.py      # Remove duplicate records
├── main.py            # Initial single-file cleaning example
├── merge.py           # Merge, clean, validate, and export CSV data
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
├── requirements.txt   # Python dependencies
├── tests/            # Automated tests for cleaning, duplicates, missing values, and export
├── .gitignore
└── README.md
```

The scripts expect a local `data/` directory for input files. The `output/` directory is created automatically when `merge.py` runs successfully.

## 🚀 Getting started

### 1. Clone the repository

```bash
git clone https://github.com/bruniibs/data-entry-toolkit.git
cd data-entry-toolkit
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows (Git Bash):

```bash
source .venv/Scripts/activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare sample data

Create a folder named `data` in the project root and add two CSV files: `clients_01.csv` and `clients_02.csv`.

Example `data/clients_01.csv`:

```csv
nome,email,cidade
  ana silva  , ANA@EXAMPLE.COM ,sao paulo
Joao Souza,joao@example.com,rio de janeiro
```

Example `data/clients_02.csv`:

```csv
nome,email,cidade
Ana Silva,ana@example.com,Sao Paulo
Maria Costa,maria@example.com,curitiba
```

Use UTF-8 encoded files with the columns shown above.

### 5. Run the processing pipeline

```bash
python merge.py
```

The pipeline reads both files, merges and standardizes their records, removes duplicates, checks the result, and exports:

```text
output/clientes_tratados.csv
```

If the output file already exists, the toolkit creates a numbered file, such as
`clientes_tratados_001.csv`, preserving previous exports.

To try the original single-file example, create `data/clients.csv` and run `python main.py`.

## 🔍 Example transformation

**Input**

| nome | email | cidade |
| --- | --- | --- |
| `  ana silva  ` | ` ANA@EXAMPLE.COM ` | `sao paulo` |
| `Ana Silva` | `ana@example.com` | `Sao Paulo` |

**Output**

| nome | email | cidade |
| --- | --- | --- |
| Ana Silva | ana@example.com | Sao Paulo |

Whitespace and capitalization are standardized, and the duplicate row is removed.

## 🧪 Validation and file safety

The merging pipeline includes checks for:

- The expected number of merged rows.
- Consistency between the number of removed duplicates and final rows.
- The absence of remaining identical rows.
- Normalized email formatting.
- Consistency between the exported CSV and the in-memory DataFrame.

The current export uses exclusive file creation (`x` mode), preventing accidental overwrites of an existing output CSV. This is a useful safeguard, but not a substitute for backups or full production-grade validation.

## 🧪 Running automated tests

With your virtual environment activated, install pytest if needed:

```bash
python -m pip install pytest
```

Run the test suite from the project root:

```bash
python -m pytest -q
```

The tests cover data standardization, required columns, duplicate removal,
missing value normalization, missing value reports, and CSV export.

## 🛠️ Built with

- **Python** — processing logic and automation.
- **Pandas** — tabular data manipulation, CSV handling, and validation.
- **pathlib** — output file and directory management.

## 🗺️ Roadmap

- [x] Standardize text fields
- [x] Remove duplicate records
- [x] Merge CSV datasets
- [x] Add basic integration assertions
- [x] Export CSV without overwriting existing output
- [x] Validate exported CSV contents
- [x] Add automated tests for cleaning, duplicates, missing values, and export
- [x] Validate required columns before cleaning
- [x] Normalize missing values and report counts by column
- [ ] Add reusable test datasets
- [ ] Expand validation for invalid inputs
- [ ] Support configurable file paths and column mappings
- [ ] Build a user-friendly command-line interface
- [ ] Expand support for Excel files (`.xlsx`)
- [ ] Generate more detailed data quality reports

## 🎯 Why I built this

I started this project to strengthen my Python and data-processing skills while building useful tools for real-world **data entry, data cleaning, and freelance automation** workflows.

It also serves as a hands-on learning project focused on readable code, modular design, data integrity, and safer file operations.

## 👩‍💻 Author

**Bruna Sant'Ana**  
Computer Science student · Python & automation enthusiast

[GitHub @bruniibs](https://github.com/bruniibs)

---

<div align="center">

<sub>Made with Python · Learning through building</sub>

</div>
