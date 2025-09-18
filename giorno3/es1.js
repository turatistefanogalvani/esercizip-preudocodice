const n = parseInt(prompt("Inserisci un numero:"));
let fattoriale = 1;

for (let i = 1; i <= n; i++) {
    fattoriale *= i;
}

console.log(`Il fattoriale di ${n} è: ${fattoriale}`);
