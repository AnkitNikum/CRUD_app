var opr = '{{opr}}';
    var table_list1 = {{table_list|tojson}};
    var head_line = document.createElement("h1");
    head_line.innerHTML = 'Please select the table you want to '+opr+' data in from '+ '{{db}} ';
    head_line.style = "text-align: center"
    document.getElementById("div1").appendChild(head_line);
    document.getElementById("div1").appendChild(document.createElement("br"));
    form1 = document.createElement("form")
    if (opr == 'update'){
    form1.action = "update1";}
    else if(opr =='show'){
        form1.action = "show1"
    }
    else if(opr =='delete'){
        form1.action = "delete1"
    }
    else{form1.action = "insert2"}
    form1.method = "POST"
    select1 = document.createElement("select")
    select1.id = "Table_option"
    select1.name = "Tables"
    table_list1.forEach(element => {
        option1 = document.createElement("option")
        option1.innerHTML = element
        option1.value = element
        select1.appendChild(option1)    
    });
    form1.appendChild(select1)
    var br = document.createElement("br");
    form1.appendChild(br);
    br = document.createElement("br");
    form1.appendChild(br)
    if(opr == 'delete'){
    select1 = document.createElement("select")
    select1.id = "del_option"
    select1.name = "del_opt"
    option1 = document.createElement("option")
    option1.innerHTML = "DELETE TABLE"
    option1.value = "delete"
    select1.appendChild(option1)    
    option1 = document.createElement("option")
    option1.innerHTML = "DROP TABLE"
    option1.value = "drop"
    select1.appendChild(option1)
    form1.appendChild(select1)
    br = document.createElement("br");
    form1.appendChild(br);
    br = document.createElement("br");
    form1.appendChild(br)
    }
    if ((opr == 'update') || (opr == 'show') || (opr == 'delete')){
    let y = document.createElement("input")
    var t = document.createTextNode('Any where clause filters'+'\xa0\xa0');
    y.setAttribute("type", "text");
    y.setAttribute("Placeholder", "value");
    y.setAttribute("Name", "where");
    br = document.createElement("br");
    form1.appendChild(t);
    form1.appendChild(y);
    form1.appendChild(br);
     }
    br = document.createElement("br");
    form1.appendChild(br);
    btn = document.createElement("button")
    btn.innerHTML = "Submit"
    btn.type = "submit"
    form1.appendChild(btn)
    document.getElementById("div2").appendChild(form1)