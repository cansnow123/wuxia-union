Sub ͸����ذ�ս��()
    '����
    Sheets("͸����").Select
    Range("A2:C50").Select
    Range("C50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("E2:G50").Select
    Range("G50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("I2:K50").Select
    Range("K50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '����
    Sheets("͸����").Select
    Range("M2:O50").Select
    Range("O50").Activate
    Selection.Copy
    Sheets("��ս�ܰ�").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
End Sub

Sub ��սͳ�Ƴ�͸����()
    '����ͳ��
        Sheets("͸����").Select
    Range("A1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C1:R107C3", Version:=6).CreatePivotTable TableDestination:= _
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
    '����ͳ��
        Sheets("͸����").Select
    Range("E1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C5:R107C7", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C5", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 5).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
    '����ͳ��
        Sheets("͸����").Select
    Range("I1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C9:R107C11", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C9", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 9).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
    '����ͳ��
        Sheets("͸����").Select
    Range("M1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "��ս�ܰ�!R1C13:R107C15", Version:=6).CreatePivotTable TableDestination:= _
        "͸����!R1C13", TableName:="����ͳ��", DefaultVersion:=6
    Sheets("͸����").Select
    Cells(1, 13).Select
    With ActiveSheet.PivotTables("����ͳ��").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("KILL"), "�����:KILL", xlSum
    ActiveSheet.PivotTables("����ͳ��").AddDataField ActiveSheet.PivotTables("����ͳ��" _
        ).PivotFields("ASS"), "�����:ASS", xlSum
End Sub
