Sub 全联盟信息()

	'帮派数字填充
	Sheets("逐梦-箱子").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "1"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("如梦-箱子").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "2"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("若梦-箱子").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "3"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("何梦-箱子").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "4"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("逐梦-箱子").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
    ActiveSheet.Paste
	
	'帮派箱子发放填充
	Sheets("如梦-箱子").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
    ActiveSheet.Paste
	
	Sheets("若梦-箱子").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
	ActiveSheet.Paste
	
	Sheets("何梦-箱子").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
	ActiveSheet.Paste
	
	'帮派数字转移
	Columns("G:G").Select
    Selection.Cut
    Columns("B:B").Select
    Selection.Insert Shift:=xlToRight
	
	'选中
	Range("A1:H1").Select
	Range(Selection, Selection.End(xlDown)).Select
	
    
End Sub