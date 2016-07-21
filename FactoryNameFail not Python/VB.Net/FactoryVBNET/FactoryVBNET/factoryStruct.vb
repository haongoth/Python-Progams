Public MustInherit Class Factory
    Public MustOverride Sub makeProduct()
End Class

Public Class USFactory
    Inherits Factory

    Public Overrides Sub makeProduct()
        Throw New NotImplementedException()
    End Sub
End Class

Public Class NonUSFactory
    Inherits Factory

    Public Overrides Sub makeProduct()
        Throw New NotImplementedException()
    End Sub
End Class

Public Class USSatcom
    Inherits USFactory

    Public Overrides Sub makeProduct()
        System.Console.WriteLine("These products make by Satcom department in US")
    End Sub
End Class

Public Class USCATV
    Inherits USFactory

    Public Overrides Sub makeProduct()
        Console.WriteLine("These products make by CATV department in US")
    End Sub
End Class

Public Class NonUSSatcom
    Inherits NonUSFactory

    Public Overrides Sub makeProduct()
        Console.WriteLine("These products make by Satcom department in Thailand")
    End Sub
End Class

Public Class NonUSCATV
    Inherits NonUSFactory

    Public Overrides Sub makeProduct()
        Console.WriteLine("These products make by CATV department in China")
    End Sub
End Class