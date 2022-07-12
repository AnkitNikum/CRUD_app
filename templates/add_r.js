function add(){
    $("form > p:nth-child(4)").clone(true).insertBefore("form > p:nth-child(4)");
    return false;
}

function remove() {
    $("form > p:nth-child(4)").remove();
}
function add1(){
    $("form > p:nth-last-child(3)").clone(true).insertBefore("form >p:nth-last-child(2)");
    return false;
}

function remove1() {
    $("form > p:nth-last-child(3)").remove()}
// FormGet Online Form Builder JS Code
// Creating and Adding Dynamic Form Elements.
var i = 1; // Global Variable for Name
var j = 1; // Global Variable for E-mail
/*
=================
Creating Text Box for name field in the Form.
=================
*/
function AttributeBoxCreate(){
var y = document.createElement("INPUT");
var t = document.createTextNode("AttributeName ");
y.setAttribute("type", "text");
y.setAttribute("Placeholder", "AttributeName_" + i);
y.setAttribute("Name", "AttributeName_" + i);
document.getElementById("myf1").appendChild(t);
document.getElementById("myf1").appendChild(y);
// t = document.createTextNode("Datatype ");
// y = document.createElement("INPUT");
// y.setAttribute("type", "text");
// y.setAttribute("Placeholder", "Datatype_" + i);
// y.setAttribute("Name", "Datatype_" + i);
// document.getElementById("myf1").appendChild(t);
// document.getElementById("myf1").appendChild(y);
// y = document.createElement("INPUT");
// t = document.createTextNode("Constraint ");
// y.setAttribute("type", "text");
// y.setAttribute("Placeholder", "Constraint_" + i);
// y.setAttribute("Name", "Constraint_" + i);
// document.getElementById("myf1").appendChild(t);
// document.getElementById("myf1").appendChild(y);
i++;
}
/*
=================
Creating Text Box for email field in the Form.
=================
*/
function FKBoxCreate(){
    var y = document.createElement("INPUT");
    var t = document.createTextNode("AttributeName ");
    y.setAttribute("type", "text");
    y.setAttribute("Placeholder", "AttributeName_" + j);
    y.setAttribute("Name", "refattrname_" + j);
    document.getElementById("myf2").appendChild(t);
    document.getElementById("myf2").appendChild(y);
    t = document.createTextNode("Refrence Table ");
    y = document.createElement("INPUT");
    y.setAttribute("type", "text");
    y.setAttribute("Placeholder", "refrencetables_" + j);
    y.setAttribute("Name", "refrencetables_" + j);
    document.getElementById("myf2").appendChild(t);
    document.getElementById("myf2").appendChild(y);
    y = document.createElement("INPUT");
    t = document.createTextNode("Refrence attribute ");
    y.setAttribute("type", "text");
    y.setAttribute("Placeholder", "refattr_" + j);
    y.setAttribute("Name", "refattr_" + j);
    document.getElementById("myf2").appendChild(t);
    document.getElementById("myf2").appendChild(y);
    j++;
    }