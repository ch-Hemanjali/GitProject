var prompt = require('prompt-sync')();

let menu ={
    Dosa : 90,idli : 99,pizza : 80,salad :88,vada : 77}
    //for (let i in menu){
        //console.log(i+" : "+ menu[i])
let cart =[];
flag =true
console.log(cart.length)
while(flag){
    let dishname = prompt("enter the dish in cart");
    if (dishname =="over") break;
    if (menu.hasOwnProperty(dishname)){
        let myorder = {
        dishname: dishname,
        price : menu[dishname]
    }
    cart.push(myorder)
}
else
    console.log("item not in the menu")
console.log(cart.length)
}

