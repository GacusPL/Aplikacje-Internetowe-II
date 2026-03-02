<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Ankieta.aspx.cs" Inherits="Zad1_kontrolki_serwerowe.Ankieta" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">


<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <asp:MultiView ID="mainMultiView" runat="server">
    
    <asp:View ID="ankietaGlowna" runat="server">
        <h3>Dane podstawowe</h3>
        Imię: <asp:TextBox ID="imieTextBox" runat="server"></asp:TextBox>
        <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" ControlToValidate="imieTextBox" ErrorMessage="Imię jest wymagane.">*</asp:RequiredFieldValidator>
        <br />
        Płeć: 
        <asp:DropDownList ID="plecDropDownList" runat="server">
            <asp:ListItem Text="Kobieta" Value="K"></asp:ListItem>
            <asp:ListItem Text="Mężczyzna" Value="M"></asp:ListItem>
            <asp:ListItem Text="Nie podaję" Value="N" Selected="True"></asp:ListItem>
        </asp:DropDownList><br />
        
        E-mail: <asp:TextBox ID="emailTextBox" runat="server"></asp:TextBox>
        <asp:RequiredFieldValidator ID="RequiredFieldValidator2" runat="server" ControlToValidate="emailTextBox" ErrorMessage="Pole E-mail jest wymagane.">*</asp:RequiredFieldValidator>
        <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" ControlToValidate="emailTextBox" ErrorMessage="Nieprawidłowy adres E-mail." ValidationExpression="\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*">*</asp:RegularExpressionValidator>
        <br />
        Telefon: <asp:TextBox ID="telTextBox" runat="server"></asp:TextBox>
        <asp:RegularExpressionValidator ID="RegularExpressionValidator2" runat="server" ControlToValidate="telTextBox" ErrorMessage="Nieprawidłowy numer telefonu: podaj same cyfry." ValidationExpression="([0-9]+)$">*</asp:RegularExpressionValidator>
        <br />
        Ulica: <asp:TextBox ID="ulicaTextBox" runat="server"></asp:TextBox><br />
        Numer domu: <asp:TextBox ID="domTextBox" runat="server"></asp:TextBox><br />
        Numer mieszkania: <asp:TextBox ID="mieszTextBox" runat="server"></asp:TextBox><br />
        Kod pocztowy: <asp:TextBox ID="kodTextBox" runat="server"></asp:TextBox><br />
        Miejscowość: <asp:TextBox ID="miejscTextBox" runat="server"></asp:TextBox>
        <br />
        <br />
        
        <hr />

        <asp:MultiView ID="ankietaMultiView" runat="server">
            
            <asp:View ID="nowyView" runat="server">
                <h4>Ankieta - Nowy Rower</h4>
                Wzrost: <asp:TextBox ID="wzrostTextBox" runat="server"></asp:TextBox>
                <asp:RegularExpressionValidator ID="RegularExpressionValidator3" runat="server" ControlToValidate="wzrostTextBox" ErrorMessage="Nieprawidłowy wzrost - podaj wzrost w centymetrach." ValidationExpression="([0-9]+)$">*</asp:RegularExpressionValidator>
                <asp:RangeValidator ID="RangeValidator1" runat="server" ControlToValidate="wzrostTextBox" ErrorMessage="Podaj poprawny wzrost w zakresie od 50 do 250 cm." MaximumValue="250" MinimumValue="50" Type="Integer">*</asp:RangeValidator>
                <br />
                Rama roweru: 
                <asp:DropDownList ID="ramaDropDownList" runat="server">
                    <asp:ListItem Text="Damska" Value="D"></asp:ListItem>
                    <asp:ListItem Text="Męska" Value="M"></asp:ListItem>
                    <asp:ListItem Text="Nie ma znaczenia" Value="N" Selected="True"></asp:ListItem>
                </asp:DropDownList><br />
                
                Marka: 
                <asp:ListBox ID="markaListBox" runat="server">
                    <asp:ListItem Text="Cateye" Value="C"></asp:ListItem>
                    <asp:ListItem Text="Giant" Value="G"></asp:ListItem>
                    <asp:ListItem Text="Kenda" Value="Ke"></asp:ListItem>
                    <asp:ListItem Text="Kross" Value="Kr"></asp:ListItem>
                    <asp:ListItem Text="Nie ma znaczenia" Value="N" Selected="True"></asp:ListItem>
                </asp:ListBox><br />
                
                Rodzaj roweru:
                <asp:ListBox ID="rodzajListBox" runat="server">
                    <asp:ListItem Text="Górski" Value="G"></asp:ListItem>
                    <asp:ListItem Text="Miejski" Value="M"></asp:ListItem>
                    <asp:ListItem Text="Szosowy" Value="S"></asp:ListItem>
                    <asp:ListItem Text="BMX" Value="B"></asp:ListItem>
                    <asp:ListItem Text="Dziecięcy" Value="D"></asp:ListItem>
                    <asp:ListItem Text="Nie wiem" Value="N" Selected="True"></asp:ListItem>
                </asp:ListBox><br />
                
                Kwota planowanych wydatków:
                <asp:RadioButtonList ID="cenaRadioButtonList" runat="server">
                    <asp:ListItem Text="Nie ma znaczenia" Value="0" Selected="True"></asp:ListItem>
                    <asp:ListItem Text="do 500 zł" Value="5"></asp:ListItem>
                    <asp:ListItem Text="500 – 1000 zł" Value="10"></asp:ListItem>
                    <asp:ListItem Text="1000 - 1500" Value="15"></asp:ListItem>
                    <asp:ListItem Text="pow. 1500" Value="20"></asp:ListItem>
                    <asp:ListItem Text="Zakres:" Value="1"></asp:ListItem>
                </asp:RadioButtonList>
                od: <asp:TextBox ID="odTextBox" runat="server" Width="50px"></asp:TextBox> 
                <asp:RegularExpressionValidator ID="RegularExpressionValidator5" runat="server" ControlToValidate="odTextBox" ErrorMessage="Nieprawidłowa kwota – podaj zaokrąglając do pełnych złotych." ValidationExpression="([0-9]+)$">*</asp:RegularExpressionValidator>
                do: <asp:TextBox ID="doTextBox" runat="server" Width="50px"></asp:TextBox>
                <asp:RegularExpressionValidator ID="RegularExpressionValidator6" runat="server" ControlToValidate="doTextBox" ErrorMessage="Nieprawidłowa kwota – podaj zaokrąglając do pełnych złotych." ValidationExpression="([0-9]+)$">*</asp:RegularExpressionValidator>
                <asp:CompareValidator ID="CompareValidator1" runat="server" ControlToCompare="odTextBox" ControlToValidate="doTextBox" ErrorMessage="Wartość w polu Do musi być większa od wartości w polu Od." Operator="GreaterThan" Type="Integer">*</asp:CompareValidator>
                <br />
                <br />
            </asp:View>

            <asp:View ID="wycieczkiView" runat="server">
                <h4>Ankieta - Posiadany Rower</h4>
                Rodzaj posiadanego roweru:
                <asp:ListBox ID="posiadaListBox" runat="server">
                    <asp:ListItem Text="Górski" Value="G"></asp:ListItem>
                    <asp:ListItem Text="Miejski" Value="M"></asp:ListItem>
                    <asp:ListItem Text="Szosowy" Value="S"></asp:ListItem>
                    <asp:ListItem Text="BMX" Value="B"></asp:ListItem>
                    <asp:ListItem Text="Dziecięcy" Value="D"></asp:ListItem>
                    <asp:ListItem Text="Nie wiem" Value="N" Selected="True"></asp:ListItem>
                </asp:ListBox>
                <br />
                <br />
                
                Data ostatniej wycieczki:
                <asp:Calendar ID="ostatniaCalendar" runat="server"></asp:Calendar><br />
                
                Data następnej wycieczki:
                <asp:Calendar ID="nastepnaCalendar" runat="server"></asp:Calendar><br />
                
                Ilość kilometrów średnio na jednej wycieczce: <asp:TextBox ID="kmTextBox" runat="server"></asp:TextBox><br />
                
                Poziom umiejętności:
                <asp:DropDownList ID="poziomDropDownList" runat="server">
                    <asp:ListItem Text="Początkujący" Value="P"></asp:ListItem>
                    <asp:ListItem Text="Średniozaawansowany" Value="S"></asp:ListItem>
                    <asp:ListItem Text="Zaawansowany" Value="Z"></asp:ListItem>
                </asp:DropDownList>
                <br />
                <br />
            </asp:View>
            
        </asp:MultiView>

        <hr />
        Preferowany rodzaj kontaktu:
        <asp:CheckBoxList ID="kontaktCheckBoxList" runat="server">
            <asp:ListItem Text="E-Mail" Value="E"></asp:ListItem>
            <asp:ListItem Text="Telefon" Value="T"></asp:ListItem>
            <asp:ListItem Text="Osobisty" Value="O"></asp:ListItem>
        </asp:CheckBoxList><br />
        
        <asp:Button ID="wyslijButton" runat="server" Text="Wyświetl" OnClick="wyslijButton_Click" />

        <br />

    </asp:View>

    <asp:View ID="podsumowanie" runat="server">
        <h3>Dziękujemy za wypełnienie ankiety!</h3>
        <a href="Default.aspx">Wróć do strony głównej</a><br />
    </asp:View>

</asp:MultiView>
        <div>
            <asp:ValidationSummary ID="ValidationSummary1" runat="server" />
        </div>
    </form>
</body>
</html>
