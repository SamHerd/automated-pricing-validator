Sub MatchAndFillPrices_Final()
    Dim wsRetail As Worksheet, wsMaster As Worksheet
    Dim lastRowRetail As Long, lastRowMaster As Long
    Dim rngRetail As Range, rngMaster As Range
    Dim cell As Range
    Dim i As Integer
    Dim masterSKU As String, retailerSKU As String
    Dim bestMatch As String
    Dim bestPrice As Variant ' Variant allows handling of both numbers and text
    Dim matchFound As Boolean

    ' Set worksheets
    Set wsRetail = ThisWorkbook.Sheets("RetailerSheet") ' Change to actual retailer sheet name
    Set wsMaster = ThisWorkbook.Sheets("MasterSheet") ' Change to actual master sheet name

    ' Find last row in each sheet
    lastRowRetail = wsRetail.Cells(wsRetail.Rows.Count, 1).End(xlUp).Row
    lastRowMaster = wsMaster.Cells(wsMaster.Rows.Count, 1).End(xlUp).Row

    ' Set ranges
    Set rngRetail = wsRetail.Range("A2:A" & lastRowRetail) ' Retailer SKUs in Column A
    Set rngMaster = wsMaster.Range("A2:C" & lastRowMaster) ' Master SKUs in Column A, Descriptions in B, Prices in C

    ' Loop through retailer SKUs
    For Each cell In rngRetail
        If Not IsEmpty(cell.Value) Then
            retailerSKU = Trim(LCase(CStr(cell.Value))) ' Convert to text, trim spaces, and lowercase
            bestMatch = ""
            bestPrice = 0
            matchFound = False

            ' Remove non-alphanumeric characters (optional)
            retailerSKU = Replace(Replace(Replace(retailerSKU, "-", ""), " ", ""), ".", "")

            ' Loop through master SKUs
            For i = 2 To lastRowMaster
                If Not IsEmpty(wsMaster.Cells(i, 1).Value) Then
                    masterSKU = Trim(LCase(CStr(wsMaster.Cells(i, 1).Value))) ' Convert master SKU to text
                    masterSKU = Replace(Replace(Replace(masterSKU, "-", ""), " ", ""), ".", "")

                    ' Check for exact match
                    If masterSKU = retailerSKU Then
                        bestMatch = masterSKU
                        bestPrice = wsMaster.Cells(i, 3).Value ' Get price from Column C in master sheet
                        matchFound = True
                        Exit For
                    End If

                    ' Check for partial match (if retailer SKU appears in master SKU or vice versa)
                    If InStr(1, masterSKU, retailerSKU, vbTextCompare) > 0 Or InStr(1, retailerSKU, masterSKU, vbTextCompare) > 0 Then
                        bestMatch = masterSKU
                        bestPrice = wsMaster.Cells(i, 3).Value ' Get price from Column C in master sheet
                        matchFound = True
                        Exit For
                    End If
                End If
            Next i

            ' Assign the best match price to Column C (instead of overwriting Column B)
            If matchFound Then
                cell.Offset(0, 2).Value = bestPrice ' Put price in Column C (2 columns to the right of SKU)
                cell.Interior.ColorIndex = xlNone ' Remove highlight if found
            Else
                ' Highlight unmatched SKUs for manual review
                cell.Interior.Color = RGB(255, 200, 200)
            End If
        End If
    Next cell

    MsgBox "Price Matching Complete! Check highlighted cells for unmatched SKUs.", vbInformation
End Sub

