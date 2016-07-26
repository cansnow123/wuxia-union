Sub 全联盟信息()
	Sheets("逐梦-箱子").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
    ActiveSheet.Paste
	
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
	
	Columns("G:G").Select
    Selection.Cut
    Columns("B:B").Select
    Selection.Insert Shift:=xlToRight
    
End Sub