<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="Zad1_kontrolki_serwerowe.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Strona główna</title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            Strona Główna<br />
            <br />
            <a href="Ankieta.aspx?view=nowy">Ankieta dla nowych klientów</a> <br /> 
            <a href="Ankieta.aspx?view=wycieczki">Ankieta dla osób posiadających rower</a>
        </div>
    </form>
</body>
</html>
