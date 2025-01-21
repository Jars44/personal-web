let inputSaatIni = '';

function tambahkanAngka(angka) {
    inputSaatIni += angka;
    perbaruiHasil();
}

function tambahkanOperator(operator) {
    if (inputSaatIni !== '' && !isNaN(inputSaatIni.slice(-1))) {
        inputSaatIni += operator;
        perbaruiHasil();
    }
}

function hitungHasil() {
    try {
        const hasil = evaluateExpression(inputSaatIni);
        inputSaatIni = hasil.toString();
        perbaruiHasil();
    } catch (error) {
        inputSaatIni = 'Error';
        perbaruiHasil();
    }
}

function evaluateExpression(expression) {
    const operators = /[+\-*\/]/;
    const numbers = expression.split(operators);
    const operations = expression.match(operators);
    
    let result = parseFloat(numbers[0]);

    for (let i = 0; i < operations.length; i++) {
        const nextNumber = parseFloat(numbers[i + 1]);
        switch (operations[i]) {
            case '+':
                result += nextNumber;
                break;
            case '-':
                result -= nextNumber;
                break;
            case '*':
                result *= nextNumber;
                break;
            case '/':
                result /= nextNumber;
                break;
        }
    }

    return result;
}

function hapusKarakter() {
    inputSaatIni = inputSaatIni.slice(0, -1);
    perbaruiHasil();
}

function bersihkanHasil() {
    inputSaatIni = '';
    perbaruiHasil();
}

function perbaruiHasil() {
    document.getElementById('hasil').value = inputSaatIni;
}