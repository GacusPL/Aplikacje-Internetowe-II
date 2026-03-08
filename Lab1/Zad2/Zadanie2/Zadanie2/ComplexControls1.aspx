<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="ComplexControls1.aspx.cs" Inherits="Zadanie2.WebForm1" %>

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
            
            Wybierz hymn:
            <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="true" OnSelectedIndexChanged="DropDownList1_SelectedIndexChanged">
                <asp:ListItem Text="polski" Value="polski"></asp:ListItem>
                <asp:ListItem Text="angielski" Value="angielski"></asp:ListItem>
                <asp:ListItem Text="francuski" Value="francuski"></asp:ListItem>
            </asp:DropDownList>
            
            <hr />

            <asp:MultiView ID="MultiView1" runat="server" ActiveViewIndex="0">
                
                <asp:View ID="View1" runat="server">
                    <p>
                        Jeszcze Polska nie zginęła,<br />
                        Kiedy my żyjemy.<br />
                        Co nam obca przemoc wzięła,<br />
                        Szablą odbierzemy.
                    </p>
                    <asp:LinkButton ID="LinkButton1" runat="server" Text="Poprzedni" CommandName="PrevView" Enabled="false"></asp:LinkButton> | 
                    <asp:LinkButton ID="LinkButton2" runat="server" Text="Następny" CommandName="NextView"></asp:LinkButton>
                </asp:View>

                <asp:View ID="View2" runat="server">
                    <p>
                        God save our gracious Queen<br />
                        Long live our noble Queen<br />
                        God save the Queen!<br />
                        Send her victorious<br />
                        Happy and glorious<br />
                        Long to reign over us<br />
                        God save the Queen!
                    </p>
                    <asp:LinkButton ID="LinkButton3" runat="server" Text="Poprzedni" CommandName="PrevView"></asp:LinkButton> | 
                    <asp:LinkButton ID="LinkButton4" runat="server" Text="Następny" CommandName="NextView"></asp:LinkButton>
                </asp:View>

                <asp:View ID="View3" runat="server">
                    <p>
                        Allons enfants de la Patrie<br />
                        Le jour de gloire est arrivé!<br />
                        Contre nous de la tyrannie<br />
                        L'étendard sanglant est levé (bis)
                    </p>
                    <asp:LinkButton ID="LinkButton5" runat="server" Text="Poprzedni" CommandName="PrevView"></asp:LinkButton> | 
                    <asp:LinkButton ID="LinkButton6" runat="server" Text="Następny" CommandName="NextView" Enabled="false"></asp:LinkButton>
                </asp:View>

            </asp:MultiView>

        </ContentTemplate>
    </asp:UpdatePanel>
</div>
        </div>
    </form>
</body>
</html>
