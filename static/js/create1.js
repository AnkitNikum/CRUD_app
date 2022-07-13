// function add(){
//     $("form > p:nth-child(4)").clone(true).insertBefore("form > p:nth-child(4)");
//     return false;
// }

function remove() {
    // $("form > p:nth-child(4)").remove();
     let l1 = document.getElementById("myf11");
     l1.remove();
 }
 // function add1(){
 //     $("form > p:nth-last-child(3)").clone(true).insertBefore("form >p:nth-last-child(2)");
 //     return false;
 // }
 
 function remove1() {
    // $("form > p:nth-last-child(3)").remove()
    let l1 = document.getElementById("myf21");
    l1.remove();}
 // FormGet Online Form Builder JS Code
 // Creating and Adding Dynamic Form Elements.
 var i = 2; // Global Variable for Name
 var j = 2; // Global Variable for E-mail
 /*
 =================
 Creating Text Box for name field in the Form.
 =================
 */
 
  function AttributeBoxCreate(){
 // let par =`<p id = "myf1${i}"> Attribute Name &nbsp &nbsp<input type="text" name = "Aname_${i}" >
 //               Data Type &nbsp &nbsp<input type="text" name = "dt_${i}">
 //               AUTO INCREMENT &nbsp &nbsp<input type="checkbox" name="auto_${i}" >
 //               Constraint (please don't enter foreign key) &nbsp &nbsp<input type="text" name = "con_${i}" >
 //             <button onclick="remove()" type="button">Remove</button><br><br></p>`;
 // document.getElementById("f1").innerHTML +=par;
 const para = document.createElement("p"); 
 para.id = "myf1" + i;
 var y = document.createElement("INPUT");
 var t = document.createTextNode("AttributeName "+'\xa0\xa0');
 y.setAttribute("type", "text");
 y.setAttribute("Placeholder", "AttributeName_" + i);
 y.setAttribute("Name", "Aname_" + i);
 para.appendChild(t);
 para.appendChild(y);
 t = document.createTextNode('\xa0\xa0'+"Datatype "+'\xa0\xa0');
 y = document.createElement("INPUT");
 y.setAttribute("type", "text");
 y.setAttribute("Placeholder", "Datatype_" + i);
 y.setAttribute("Name", "dt_" + i);
 para.appendChild(t);
 para.appendChild(y);
 t = document.createTextNode('\xa0\xa0'+"AUTO INCREMENT "+'\xa0\xa0');
 y = document.createElement("INPUT");
 y.setAttribute("type", "checkbox");
 y.setAttribute("Name", "auto_" + i);
 para.appendChild(t);
 para.appendChild(y);
 y = document.createElement("INPUT");
 t = document.createTextNode('\xa0\xa0'+"Constraint "+'\xa0\xa0');
 y.setAttribute("type", "text");
 y.setAttribute("Placeholder", "Constraint_" + i);
 y.setAttribute("Name", "con_" + i);
 para.appendChild(t);
 para.appendChild(y);
 let btn = document.createElement("button");
 btn.innerHTML = "Remove";
 btn.type = "button";
 btn.id = "b1"+i;
 btn.addEventListener('click', function handleClick(event) {
   // 👇️ "parent"
   const child = document.getElementById(btn.id);
   console.log(btn.id)
   let id1 = child.parentElement.id;
   let l1 = document.getElementById(id1);
     l1.remove()
 }); 
 //var b_1 = b.cloneNode(true)
 para.appendChild(btn);
 var br = document.createElement("br");
 para.appendChild(br);
 br = document.createElement("br");
 para.appendChild(br);
 document.getElementById("f1").appendChild(para);
 i++;
 }
 /*
 =================
 Creating Text Box for email field in the Form.
 =================
 */
 function FKBoxCreate(){
     // let par =`<p id = "myf2${j}">  Attribute Name &nbsp &nbsp<input type="text"  name = "Rname_${j}" >
     //             Refrence Table &nbsp &nbsp<input type="text" name = "RT_${j}" >
     //             Refrence attribute &nbsp &nbsp<input type="text" name = "RA_${j}" >
     //           <button  onclick="remove1()" type="button">Remove</button><br><br></p>`;
     // document.getElementById("f2").innerHTML +=par;
     const para = document.createElement("p");
     para.id = "myf2" + j;
     var y = document.createElement("INPUT");
     var t = document.createTextNode("AttributeName "+ '\xa0\xa0');
     y.setAttribute("type", "text");
     y.setAttribute("Placeholder", "refattrname_" + j);
     y.setAttribute("Name", "Rname_" + j);
     para.appendChild(t);
     para.appendChild(y);
     t = document.createTextNode('\xa0\xa0'+"Refrence Table "+'\xa0\xa0');
     y = document.createElement("INPUT");
     y.setAttribute("type", "text");
     y.setAttribute("Placeholder", "refrencetable_" + j);
     y.setAttribute("Name", "RT_" + j);
     para.appendChild(t);
     para.appendChild(y);
     y = document.createElement("INPUT");
     t = document.createTextNode('\xa0\xa0'+"Refrence attribute "+'\xa0\xa0');
     y.setAttribute("type", "text");
     y.setAttribute("Placeholder", "refattr_" + j);
     y.setAttribute("Name", "RA_" + j);
     para.appendChild(t);
     para.appendChild(y);
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
        l1.remove()
 });
 //var b_1 = b.cloneNode(true)
 para.appendChild(btn);
 var br = document.createElement("br");
 para.appendChild(br);
 br = document.createElement("br");
 para.appendChild(br);
 document.getElementById("f2").appendChild(para);
     j++;
     }
setup();
