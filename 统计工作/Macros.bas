Sub 透明表回帮战表()
    '逐梦
    Sheets("透明表").Select
    Range("A2:D50").Select
    Range("D50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '如梦
    Sheets("透明表").Select
    Range("F2:I50").Select
    Range("I50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '若梦
    Sheets("透明表").Select
    Range("K2:N50").Select
    Range("N50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    '何梦
    Sheets("透明表").Select
    Range("P2:S50").Select
    Range("S50").Activate
    Selection.Copy
    Sheets("帮战总榜").Select
    ActiveCell.Offset(0, 5).Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
End Sub

Sub 帮战统计出透明表()
    '逐梦统计
        Sheets("透明表").Select
    Range("A1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C1:R107C4", Version:=6).CreatePivotTable TableDestination:= _
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
	ActiveSheet.PivotTables("逐梦统计").AddDataField ActiveSheet.PivotTables("逐梦统计" _
        ).PivotFields("HONOR"), "荣誉:HONOR", xlSum
    '如梦统计
        Sheets("透明表").Select
    Range("E1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C6:R107C9", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C6", TableName:="如梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 6).Select
    With ActiveSheet.PivotTables("如梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("如梦统计").AddDataField ActiveSheet.PivotTables("如梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("如梦统计").AddDataField ActiveSheet.PivotTables("如梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
    ActiveSheet.PivotTables("如梦统计").AddDataField ActiveSheet.PivotTables("如梦统计" _
        ).PivotFields("HONOR"), "荣誉:HONOR", xlSum
	'若梦统计
        Sheets("透明表").Select
    Range("I1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C11:R107C14", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C11", TableName:="若梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 11).Select
    With ActiveSheet.PivotTables("若梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("若梦统计").AddDataField ActiveSheet.PivotTables("若梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("若梦统计").AddDataField ActiveSheet.PivotTables("若梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
    ActiveSheet.PivotTables("若梦统计").AddDataField ActiveSheet.PivotTables("若梦统计" _
        ).PivotFields("HONOR"), "荣誉:HONOR", xlSum
	'何梦统计
        Sheets("透明表").Select
    Range("M1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C16:R107C19", Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C16", TableName:="何梦统计", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 16).Select
    With ActiveSheet.PivotTables("何梦统计").PivotFields("ID")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("何梦统计").AddDataField ActiveSheet.PivotTables("何梦统计" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("何梦统计").AddDataField ActiveSheet.PivotTables("何梦统计" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
	ActiveSheet.PivotTables("何梦统计").AddDataField ActiveSheet.PivotTables("何梦统计" _
        ).PivotFields("HONOR"), "荣誉:HONOR", xlSum
End Sub
