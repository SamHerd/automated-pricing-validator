# How to Set Up and Use the Streamlit Price Matcher App

## Prerequisites
Before running the app, ensure you have the following installed:

1. **Python 3.8 or higher** ([Download Here](https://www.python.org/downloads/))
2. **Required Python Libraries** (installed via `requirements.txt`)

## Installation Steps

### **1. Clone or Download the Repository**
If using Git, clone the repository:
```bash
git clone https://github.com/yourusername/streamlit-price-matcher.git
cd streamlit-price-matcher
```
Or, manually download the files from GitHub and navigate to the folder.

### **2. Install Dependencies**
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```
This installs:
- `streamlit` (for the web app interface)
- `pandas` (for data processing)
- `openpyxl` (for Excel file handling)
- `rapidfuzz` (for fuzzy SKU matching)

### **3. Run the Streamlit App**
Start the app by running:
```bash
streamlit run price_matcher.py
```
This will launch a local web server and provide a URL to access the app.

## File Format Requirements

To ensure successful processing, the uploaded files must follow this structure:

### **Retailer Workbook (CSV or Excel)**
| **UPC/SKU** | **Product Description**  | **Price** |
|------------|--------------------------|----------|
| 123456     | Sample Product 1          |          |
| 789012     | Sample Product 2          |          |

(Prices in Column C will be auto-filled by the app)

### **Master Workbook (CSV or Excel)**
| **UPC/SKU** | **Product Description**  | **Price** |
|------------|--------------------------|----------|
| 123456     | Sample Product 1          | 9.99  |
| 789012     | Sample Product 2          | 14.99 |

(Ensure that Column C contains accurate prices for each SKU)

## How to Use the App

### **1. Upload Your Files**
- Upload your **Retailer Workbook** and **Master Workbook**.
- The app will automatically match SKUs and fill in missing prices.

### **2. Review and Download**
- Unmatched SKUs will be highlighted for review.
- Download the updated **Retailer Workbook** once processing is complete.

## Alternative: Excel VBA Version
If you prefer not to use the Streamlit app, there is an alternative Excel-based solution using VBA macros.

### **How the Excel VBA Version Works**
- The Excel file contains a **macro-enabled workbook** (`.xlsm`) that automates price matching.
- Users copy and paste their **Retailer Workbook** and **Master Workbook** into designated sheets.
- A built-in VBA script matches SKUs and fills in the missing prices.
- The script highlights unmatched SKUs for manual review.
- Users can then save and export the updated file.

### **When to Use the Excel Version**
✅ If you prefer working directly in Excel.
✅ If you are not comfortable setting up Python and running scripts.
✅ If you need an offline solution without requiring a web app.

For access to the Excel VBA version, download `Pricing_Automation_VBA.xlsm` from this repository.

## Troubleshooting
- **Command not found?** Ensure Python and Streamlit are installed.
- **App not opening?** Try manually opening the URL provided in the terminal.
- **Dependency issues?** Re-run `pip install -r requirements.txt` to reinstall libraries.

Once completed, your app should be fully functional! 🚀






