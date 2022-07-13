var col_list1 = {{col_list|tojson}};
    var my_list1 = {{mylist|tojson}};
    para = document.createElement("p");
    i=0
    col_list1.forEach(element => {
           text_node = document.createTextNode(element+'\xa0\xa0:\xa0')           
           para.appendChild(text_node)
           j=0
           my_list1[i].forEach(element1 => {
           if(j < (my_list1[i].length -1)){
           text_node = document.createTextNode(element1+'\xa0\xa0,'); }
           else{
            text_node = document.createTextNode(element1+'\xa0\xa0'); } 
           j++;         
           para.appendChild(text_node);
    });
    var br = document.createElement("br");
    para.appendChild(br);
    br = document.createElement("br");
    para.appendChild(br);
    i++;
    });
    br = document.createElement("br");
    para.appendChild(br);
    
    document.getElementById("div1").appendChild(para)