Sub ȫ������Ϣ()

	'�����������
	Sheets("����-����").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "1"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("����-����").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "2"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("����-����").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "3"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("����-����").Select
    Range("G2").Select
    ActiveCell.FormulaR1C1 = "4"
    Selection.AutoFill Destination:=Range("G2:G153")
	
	Sheets("����-����").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
    ActiveSheet.Paste
	
	'�������ӷ������
	Sheets("����-����").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
    ActiveSheet.Paste
	
	Sheets("����-����").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
	ActiveSheet.Paste
	
	Sheets("����-����").Select
	Range("A2:H2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("MYSQL").Select
    Range("A1").Select
	Selection.End(xlDown).Select
	ActiveCell.Offset(1, 0).Select
	ActiveSheet.Paste
	
	'��������ת��
	Columns("G:G").Select
    Selection.Cut
    Columns("B:B").Select
    Selection.Insert Shift:=xlToRight
	
	'ѡ��
	Range("A1:H1").Select
	Range(Selection, Selection.End(xlDown)).Select
	
    
End Sub