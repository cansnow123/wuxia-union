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

Sub 帮战统计出透明表()
    '逐梦统计
        Sheets("透明表").Select
    Range("A1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C1:R107C3", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C1", TableName:="逐梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 1).Select
    With ActiveSheet.PivotTables("逐梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("逐梦统计").AddDataField ActiveSheet.PivotTables("逐梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("逐梦统计").AddDataField ActiveSheet.PivotTables("逐梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
    '如梦统计
        Sheets("透明表").Select
    Range("E1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C5:R107C7", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C5", TableName:="如梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 5).Select
    With ActiveSheet.PivotTables("如梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("如梦统计").AddDataField ActiveSheet.PivotTables("如梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("如梦统计").AddDataField ActiveSheet.PivotTables("如梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
    '若梦统计
        Sheets("透明表").Select
    Range("I1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C9:R107C11", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C9", TableName:="若梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 9).Select
    With ActiveSheet.PivotTables("若梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("若梦统计").AddDataField ActiveSheet.PivotTables("若梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("若梦统计").AddDataField ActiveSheet.PivotTables("若梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
    '何梦统计
        Sheets("透明表").Select
    Range("M1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C13:R107C15", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C13", TableName:="何梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 13).Select
    With ActiveSheet.PivotTables("何梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("何梦统计").AddDataField ActiveSheet.PivotTables("何梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("何梦统计").AddDataField ActiveSheet.PivotTables("何梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
End Sub
