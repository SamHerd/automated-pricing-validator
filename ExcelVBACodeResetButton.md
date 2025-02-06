Sub ResetRetailerSheet()
    Dim wsRetail As Worksheet
    Dim lastRow As Long
    
    ' Set worksheet
    Set wsRetail = ThisWorkbook.Sheets("RetailerSheet") ' Update to actual retailer sheet name

    ' Find the last row in Column A (SKU column)
    lastRow = wsRetail.Cells(wsRetail.Rows.Count, 1).End(xlUp).Row

    ' Clear only Column C (Price column) from row 2 to the last row
    wsRetail.Range("C2:C" & lastRow).ClearContents

    ' Remove any red highlights from Column A (unmatched SKUs)
    wsRetail.Range("A2:A" & lastRow).Interior.ColorIndex = xlNone

    MsgBox "Retailer sheet has been reset! You can now run the macro with a clean slate.", vbInformation
End Sub

