Sub ͸����ذ�ս��()
    '����
    Sheets("͸����").Select
    Range("A2:D50").Select
    Range("D50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("F2:I50").Select
    Range("I50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("K2:N50").Select
    Range("N50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("P2:S50").Select
    Range("S50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
End Sub

Sub ��սͳ�Ƴ�͸����()
    '����ͳ��
        Sheets("͸����").Select
    Range("A1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C1:R107C4", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C1", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 1).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
	ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("HONOR"), "����:HONOR", xlSum
    '����ͳ��
        Sheets("͸����").Select
    Range("E1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C6:R107C9", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C6", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 6).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("HONOR"), "����:HONOR", xlSum
	'����ͳ��
        Sheets("͸����").Select
    Range("I1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C11:R107C14", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C11", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 11).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("HONOR"), "����:HONOR", xlSum
	'����ͳ��
        Sheets("͸����").Select
    Range("M1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C16:R107C19", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C16", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 16).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
	ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("HONOR"), "����:HONOR", xlSum
End Sub
