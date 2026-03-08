<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="SimpleControls.aspx.cs" Inherits="Zadanie2.SimpleControls" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <div>
    <asp:ScriptManager ID="ScriptManager1" runat="server"></asp:ScriptManager>

    <asp:UpdatePanel ID="UpdatePanel1" runat="server">
        <ContentTemplate>
            
            <h4>Zmień styl tekstu:</h4>
            
            <asp:CheckBoxList ID="CheckBoxList1" runat="server" AutoPostBack="true" OnSelectedIndexChanged="CheckBoxList1_SelectedIndexChanged">
                <asp:ListItem Text="bold" Value="true"></asp:ListItem>
                <asp:ListItem Text="italics" Value="true"></asp:ListItem>
            </asp:CheckBoxList>
            
            <asp:RadioButtonList ID="RadioButtonList1" runat="server" AutoPostBack="true" OnSelectedIndexChanged="RadioButtonList1_SelectedIndexChanged">
                <asp:ListItem Text="8pt" Value="8"></asp:ListItem>
                <asp:ListItem Text="12pt" Value="12"></asp:ListItem>
                <asp:ListItem Text="16pt" Value="16"></asp:ListItem>
            </asp:RadioButtonList>
            
            <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="true" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged">
                <asp:ListItem Text="Times" Value="Times"></asp:ListItem>
                <asp:ListItem Text="Courier New" Value="Courier New"></asp:ListItem>
                <asp:ListItem Text="Tahoma" Value="Tahoma"></asp:ListItem>
            </asp:DropDownList>
            
            <br /><br />
            <asp:Label ID="Label1" runat="server" Text="To jest przykładowy tekst."></asp:Label>

        </ContentTemplate>
    </asp:UpdatePanel>
</div>
        </div>
    </form>
</body>
</html>
