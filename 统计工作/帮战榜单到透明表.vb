Sub 帮战统计出透明表()
    '逐梦统计
        Sheets("透明表").Select
    Range("A1").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
        "帮战总榜!R1C1:R120C3", Version:=6).CreatePivotTable TableDestination:= _
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
        "帮战总榜!R1C5:R120C7", Version:=6).CreatePivotTable TableDestination:= _
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
        "帮战总榜!R1C9:R120C11", Version:=6).CreatePivotTable TableDestination:= _
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
        "帮战总榜!R1C13:R120C15", Version:=6).CreatePivotTable TableDestination:= _
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