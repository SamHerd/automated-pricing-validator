import streamlit as st
import pandas as pd
from rapidfuzz import process, fuzz
from io import BytesIO

def match_skus(retailer_df, master_df):
    """Matches SKUs from retailer sheet with master sheet and fills in prices."""
    # Ensure all SKUs are strings to avoid TypeErrors
    retailer_df['SKU'] = retailer_df['SKU'].astype(str)
    master_df['SKU'] = master_df['SKU'].astype(str)
    
    matched_prices = []
    
    for sku in retailer_df['SKU']:
        best_match, score, row_idx = process.extractOne(
            sku, master_df['SKU'], scorer=fuzz.token_sort_ratio
        )
        
        if score >= 80:  # If the match confidence is 80% or higher
            matched_prices.append(master_df.iloc[row_idx]['Price'])
        else:
            matched_prices.append(None)  # No match found
    
    retailer_df['Price'] = matched_prices
    return retailer_df

def main():
    st.title("Auto-Fill Retailer Prices Based on Master Data")
    st.write("Upload your Retailer Sheet and Master Sheet, and the app will match SKUs and fill in the missing prices.")
    
    retailer_file = st.file_uploader("Upload Retailer Sheet (CSV or Excel)", type=["csv", "xlsx"])
    master_file = st.file_uploader("Upload Master Sheet (CSV or Excel)", type=["csv", "xlsx"])
    
    if retailer_file and master_file:
        # Load retailer sheet
        if retailer_file.name.endswith('.csv'):
            retailer_df = pd.read_csv(retailer_file)
        else:
            retailer_df = pd.read_excel(retailer_file)
        
        # Load master sheet
        if master_file.name.endswith('.csv'):
            master_df = pd.read_csv(master_file)
        else:
            master_df = pd.read_excel(master_file)
        
        # Ensure column names are correct
        required_cols = ['SKU', 'Product Description', 'Price']
        if not all(col in master_df.columns for col in required_cols) or not all(col in retailer_df.columns[:2] for col in ['SKU', 'Product Description']):
            st.error("Error: Make sure both sheets contain the required columns: SKU, Product Description, and Price (for Master Sheet).")
            return
        
        # Process matching
        updated_df = match_skus(retailer_df, master_df)
        
        # Highlight unmatched SKUs
        unmatched_rows = updated_df['Price'].isna()
        updated_df.loc[unmatched_rows, 'Price'] = "Not Found"
        
        # Display updated data
        st.write("### Processed Retailer Sheet:")
        st.dataframe(updated_df)
        
        # Convert to Excel file for download
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            updated_df.to_excel(writer, index=False, sheet_name="Updated Retailer Sheet")
        output.seek(0)
        
        st.download_button(
            label="Download Updated Retailer Sheet",
            data=output,
            file_name="Updated_Retailer_Sheet.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
