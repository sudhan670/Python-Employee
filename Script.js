let a=45;
var y=0;
var u=67;
console.log(u);
const i=78;
function jersey( t){
    this.t=t;
    return t;
}
console.log(jersey(56));

let x=3;
let r=4;
console.log(x+r);
console.log(x-r);
console.log(x*r);
console.log(r/x); 
var y=90;
switch(y){
    case 90:
        console.log("New Jersey");
    case 91:
        console.log("New York");
    case 92:
        console.log("Boston");
    default:
        console.log("USA");
} 
let ruti=['sudhan','saravanakkumar','vasanth'];
ruti.splice(1,2);
console.log(ruti);
let double=n=>n*2;
console.log(double(3));
let rot=(x,y)=>{
    for(var i=x;i<=y;i++){
         console.log(i);
    }
}
rot(1,9);
let map=new Map();
map.set(1,'num1');
map.set('1','num2');
console.log(map.get(1));
console.log(map.get('1')); 
let john={'name':'john'};
let ben={'name':'Ben'};
let visited={}
visited[john]=90;
visited[ben]=89;
console.log(visited[ben]);
let mao=([
    ['cucumber',200],
    ['pototo',300],
    ['carrot',500],
]);
for(let veg of mao.values()){
   console.log(veg);
}
for(let vegg of mao.keys()){
    console.log(vegg);
}
for(let r of mao){
    console.log(r);
} 
const age = undefined ?? 28;
console.log(age); 
console.log("sudhan");