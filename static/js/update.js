var mylist1 = {{mylist|tojson}};
var column_list1 = {{column_list|tojson}};
var dt_list = {{dt|tojson}};
var null_list1 = {{null_list|tojson}};
var key_list1 = {{key_list|tojson}};
var for_cols1 = {{for_cols|tojson}};
var ref_tbls1 = {{ref_tbls|tojson}};
var ref_cols1 = {{ref_cols|tojson}};
document.querySelector("body").onload = function() {AttributeBoxCreate()};
function AttributeBoxCreate(){
for(j=0; j<mylist1.length; j++){
 form1 = document.getElementById("formfield")
 const para = document.createElement("p"); 
 para.id = "myf1"+j;
 for(let i=0; i<column_list1.length;i++) {
     let k = 0;
     var y = document.createElement("INPUT");
     var t = document.createTextNode(column_list1[i]+'\xa0\xa0'+"Data Type:"+dt_list[i]+'\xa0\xa0');
     y.setAttribute("value", mylist1[j][i]);
     y.setAttribute("Name", column_list1[i]+j);
     var br = document.createElement("br");
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
    para.appendChild(y)
 };
 for(let m=0; m<column_list1.length;m++){
     var y1 = document.createElement("INPUT");
     y1.setAttribute("type","hidden")
     y1.setAttribute("value", mylist1[j][m]);
     y1.setAttribute("Name", column_list1[m]+j+'o');
     para.appendChild(y1);
 }; 
   
 let btn = document.createElement("button");
 btn.innerHTML = "Remove";
 btn.type = "button";
 btn.id = "b2"+j;
 btn.addEventListener('click', function handleClick(event) {
    const child = document.getElementById(btn.id);
    console.log(btn.id)
    let id1 = child.parentElement.id;
    let l1 = document.getElementById(id1);
    l1.remove();
  });
  para.appendChild(btn);
  br = document.createElement("br");
  para.appendChild(br);
  form1.appendChild(para);
  };}