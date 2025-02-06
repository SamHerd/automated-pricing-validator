How to Use the Streamlit Price Matcher App

Prerequisites

Before running the app, ensure you have the following installed:

Python 3.8 or higher (Download Here)

Required Python Libraries (installed via requirements.txt)

Installation Steps

1. Clone or Download the Repository

If using Git, clone the repository:

git clone https://github.com/yourusername/streamlit-price-matcher.git
cd streamlit-price-matcher

Or, manually download the files from GitHub and navigate to the folder.

2. Install Dependencies

Run the following command to install all required libraries:

pip install -r requirements.txt

This installs:

streamlit (for the web app interface)

pandas (for data processing)

openpyxl (for Excel file handling)

rapidfuzz (for fuzzy SKU matching)

3. Run the Streamlit App

Start the app by running:

streamlit run price_matcher.py

This will launch a local web server and provide a URL to access the app.

4. Using the App

Upload your Retailer Workbook and Master Workbook.

The app will automatically match SKUs and fill in missing prices.

Unmatched SKUs will be highlighted for review.

Download the updated Retailer Workbook once processing is complete.

5. Troubleshooting

Command not found? Ensure Python and Streamlit are installed.

App not opening? Try manually opening the URL provided in the terminal.

Dependency issues? Re-run pip install -r requirements.txt to reinstall libraries.

Once completed, your app should be fully functional! 🚀

