var j = 1;
   var column_list1 = {{column_list|tojson}};
   var dt_list = {{dt|tojson}};
   var null_list1 = {{null_list|tojson}};
   var key_list1 = {{key_list|tojson}};
   var for_cols1 = {{for_cols|tojson}};
   var ref_tbls1 = {{ref_tbls|tojson}};
   var ref_cols1 = {{ref_cols|tojson}};
 function AttributeBoxCreate(){
    form1 = document.getElementById("formfield")
    const para = document.createElement("p"); 
    para.id = "myf1"+j;
    for(let i=0; i<column_list1.length;i++) {
        let k = 0;
        var y = document.createElement("INPUT");
        var t = document.createTextNode(column_list1[i]+'\xa0\xa0');
        y.setAttribute("type", "text");
        y.setAttribute("Placeholder", "value");
        y.setAttribute("Name", column_list1[i]+j);
        var br = document.createElement("br");
        para.appendChild(t);
        para.appendChild(y);
        t = document.createTextNode('\xa0\xa0'+"Data Type:"+dt_list[i]+'\xa0\xa0');
        para.appendChild(t); 
        if(key_list1[i]=='PRI'){
            t = document.createTextNode("PRIMARY KEY"+'\xa0\xa0'); 
            para.appendChild(t)
        }
        if(key_list1[i]== 'UNI'){
            t = document.createTextNode("UNIQUE KEY"+'\xa0\xa0'); 
            para.appendChild(t)
        }
        if(null_list1[i]== 'NO'){
            t = document.createTextNode("Column not nullable"+'\xa0\xa0'); 
            para.appendChild(t)
        }
        if(for_cols1[k] == column_list1[i]){
            t = document.createTextNode("Foreign key references"+ref_tbls1[k]+'('+ref_cols1[k]+')' +'\xa0\xa0'); 
            para.appendChild(t)
            k++;
        }
         
    };
    let btn = document.createElement("button");
    btn.innerHTML = "Remove";
    btn.type = "button";
    btn.id = "b2"+j;
    btn.addEventListener('click', function handleClick(event) {
  // 👇️ "parent"
       const child = document.getElementById(btn.id);
       console.log(btn.id)
       let id1 = child.parentElement.id;
       let l1 = document.getElementById(id1);
       l1.remove();
     });
     para.appendChild(btn);
     br = document.createElement("br");
     para.appendChild(br);
     br = document.createElement("br");
     para.appendChild(br);
     form1.appendChild(para);
     j++;}