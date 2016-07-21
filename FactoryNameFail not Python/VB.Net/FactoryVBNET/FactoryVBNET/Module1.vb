Module Module1

    Sub Main()
        Dim aFactory As Factory = Nothing
        aFactory = New USCATV()
        aFactory.makeProduct()

        aFactory = New NonUSCATV
        aFactory.makeProduct()
    End Sub

End Module
