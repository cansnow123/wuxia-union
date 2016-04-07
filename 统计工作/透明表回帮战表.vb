Sub 透明表回帮战表()
    '逐梦
    Sheets("透明表").Select
    Range("A2:C50").Select
    Range("C50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '如梦
    Sheets("透明表").Select
    Range("E2:G50").Select
    Range("G50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '若梦
    Sheets("透明表").Select
    Range("I2:K50").Select
    Range("K50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '何梦
    Sheets("透明表").Select
    Range("M2:O50").Select
    Range("O50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 4).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
End Sub