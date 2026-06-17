# QR-code-generator# QR-code-generator

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat-square)
![Framework](https://img.shields.io/badge/Jupyter%20Notebook-%20-orange?style=flat-square)
![Stars](https://img.shields.io/github/stars/Joedharsic07/QR-code-generator?style=flat-square)
![Forks](https://img.shields.io/github/forks/Joedharsic07/QR-code-generator?style=flat-square)

## Overview

QR-code-generator is a lightweight Python library for generating QR codes. It leverages the `qrcode` library with PIL support to create customizable QR codes with ease. The project includes both a Python script and a Jupyter Notebook for demonstration, making it simple to integrate QR code creation into your own projects or use interactively.

## Tech Stack

- Python
- Jupyter Notebook
- [qrcode](https://pypi.org/project/qrcode/) (with PIL support)

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/Joedharsic07/QR-code-generator.git
cd QR-code-generator
pip install -r requirements.txt
```

## Usage

### Using the Python Script

Import the `QR_code_generator.py` module in your project:

```python
from QR_code_generator import generate_qr_code

# Example usage
generate_qr_code("https://example.com", output_path="example_qr.png")
```

- `generate_qr_code(data, output_path="qr.png")`: Generates a QR code for the given data and saves it to the specified path.

### Using the Jupyter Notebook

Run the included notebook for interactive examples:

```bash
jupyter notebook "QR code generator.ipynb"
```

Follow the cells to generate and customize QR codes.

### Customization

You can modify parameters such as QR code size, error correction, and output format within the script or notebook as needed.

## Project Structure

```
QR-code-generator/
│
├── .gitignore               # Git ignore rules
├── QR code generator.ipynb  # Jupyter Notebook with usage examples
├── QR_code_generator.py     # Python module for QR code generation
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
```

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes.
4. Push to your branch (`git push origin feature/my-feature`).
5. Open a Pull Request describing your changes.

## License

No license specified. If you wish to use or contribute to this project, please contact the repository owner.

---