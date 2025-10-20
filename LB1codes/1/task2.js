let num = 12345;
let count = 0;
while (num >= 1) {
    num = Math.floor(num / 10);
    count++;
}

console.log(count);
