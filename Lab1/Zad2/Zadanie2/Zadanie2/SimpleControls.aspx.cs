using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace Zadanie2
{
    public partial class SimpleControls : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void CheckBoxList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            Label1.Font.Bold = CheckBoxList1.Items[0].Selected == true;
            Label1.Font.Italic = CheckBoxList1.Items[1].Selected == true;
        }

        protected void RadioButtonList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            Label1.Font.Size = FontUnit.Point(Int32.Parse(RadioButtonList1.SelectedValue));
        }

        protected void DropDownList1_SelectedIndexChanged(object sender, EventArgs e)
        {
            Label1.Font.Name = DropDownList1.SelectedValue;
        }
    }
}