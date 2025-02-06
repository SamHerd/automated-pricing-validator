Streamlit Price Matcher App

Purpose

This Streamlit app is designed to automate the process of filling in missing prices in retailer workbooks based on a master price sheet. It reduces manual data entry errors and improves efficiency by using fuzzy matching to align SKUs.

File Format Requirements

To ensure successful processing, the uploaded files must follow this structure:

Retailer Workbook Example (CSV or Excel)

| **UPC/SKU**| **Product Description**   | **Price**|
|------------|-------------------------- |----------|
| 123456     | Sample Product 1          |          |
| 789012     | Sample Product 2          |          |

(Prices in Column C will be auto-filled by the app)

Master Workbook Example (CSV or Excel)

| **UPC/SKU**| **Product Description**  | **Price**|
|------------|--------------------------|----------|
| 123456     | Sample Product 1         |  12.99   |
| 789012     | Sample Product 2         |  15.99   |


How It Works

	1. The user uploads the Retailer Workbook and Master Workbook.

	2. The app matches SKUs using fuzzy matching.

	3. Prices from the Master Workbook are inserted into the Retailer Workbook.

	4. Unmatched SKUs are flagged for manual review.

	5. The updated Retailer Workbook can be downloaded as an Excel file.

This tool ensures accuracy and efficiency in pricing updates, saving time for businesses that handle bulk product data.
