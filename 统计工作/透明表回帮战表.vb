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