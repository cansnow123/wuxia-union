Option Explicit
Sub 透明表()
    On Error Resume Next
    Dim now_r, now_c
    ActiveCell.Select
    now_r = ActiveCell.Row()
    now_c = ActiveCell.Column()
    Sheets("帮战总榜").Select
    ActiveWorkbook.PivotCaches.Create(SourceType:=xlDatabase, SourceData:= _
       Worksheets("帮战总榜").Range(Cells(now_r, now_c), Cells(100, 1)).CurrentRegion, Version:=6).CreatePivotTable TableDestination:= _
        "透明表!R1C1", TableName:="TEST", DefaultVersion:=6
    Sheets("透明表").Select
    Cells(1, 1).Select
    With ActiveSheet.PivotTables("Test").PivotFields("id")
        .Orientation = xlRowField
        .Position = 1
    End With
    ActiveSheet.PivotTables("Test").AddDataField ActiveSheet.PivotTables("Test" _
        ).PivotFields("KILL"), "求和项:KILL", xlSum
    ActiveSheet.PivotTables("Test").AddDataField ActiveSheet.PivotTables("Test" _
        ).PivotFields("ASS"), "求和项:ASS", xlSum
End Sub

