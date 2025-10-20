let maxEven = 0;

for (let i = 1; i <= 200; i++) {
    if (i % 2 === 0 && i > maxEven) {
        maxEven = i;
    }
}

console.log(maxEven);
