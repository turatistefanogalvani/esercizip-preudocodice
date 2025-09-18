let somma = 0;

while (true) {
    let n = parseInt(prompt("Inserisci un numero (0 per terminare):"));
    if (n === 0) {
        break;
    } else {
        somma += n;
    }
    console.log("Somma attuale:", somma);
}

console.log("Somma finale:", somma);
