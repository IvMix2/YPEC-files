let num = 1234;
let p = 1;
while (num >= 1) {
    p *= num % 10;
    num = Math.floor(num / 10);
}

console.log(p);
