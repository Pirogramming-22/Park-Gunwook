/*
<div class="remaining-attempts">
    남은 횟수: <span id="attempts">${attempts}</span>
</div>
*/

/*
<div class="result-display">
    <div class="check-result">
        <div id="results">
        </div>
    </div>
</div>
*/
function numberSelect() {
    let randomNumber = [];
    for (let i=0; i<3; i++) {
        randomNum = Math.floor(Math.random() * 10);
        if (randomNumber.indexOf(randomNum) === -1) {
            randomNumber.push(randomNum)
        } else {
            i--
        }
    }

    return randomNumber;
}

ScoreSet = numberSelect();

console.log(ScoreSet[0]);
console.log(ScoreSet[1]);
console.log(ScoreSet[2]);

function check_numbers(number) {
    value1 = document.getElementById('number1').value;
    value2 = document.getElementById('number2').value;
    value3 = document.getElementById('number3').value;
    if(number === 1) {
        return value1;
    }
    if(number === 2) {
        return value2;
    }
    if(number === 3) {
        return value3;
    }
}

function createResultElement(numbers, strikes, balls) {
    const checkResult = document.createElement('div');
    checkResult.className = 'check-result';
    checkResult.style.display = 'flex';
    checkResult.style.justifyContent = 'space-between';
    checkResult.style.marginBottom = '20px';

    const numbersDiv = document.createElement('div');
    numbersDiv.textContent = numbers.join(' ');
    checkResult.appendChild(numbersDiv);

    const resultsDiv = document.createElement('div');
    resultsDiv.id = 'results';
    const separatorDiv = document.createElement('div');
    separatorDiv.textContent = ':';
    resultsDiv.appendChild(separatorDiv);
    checkResult.appendChild(resultsDiv);

    const scoreDiv = document.createElement('div');

    if (strikes === 0 && balls === 0) {
        scoreDiv.textContent = 'O';
        scoreDiv.className = 'out num-result';
    } else {
        scoreDiv.innerHTML = ` ${strikes} <span class="strike num-result">S</span> ${balls} <span class="ball num-result">B</span>`;
    }
    checkResult.appendChild(scoreDiv);

    return checkResult;
}

let Strike = 0;
let Ball = 0;

let attemptSpan = 9;
const attemptsSpan = document.getElementById('attempts');

function updateAttempts(newAttempts) {
    attemptsSpan.textContent = newAttempts;
}

updateAttempts(attemptSpan);


document.querySelector('.submit-button').addEventListener('click', () => {
    const number1 = check_numbers(1);
    const number2 = check_numbers(2);
    const number3 = check_numbers(3);

    // 스트라이크 및 볼 계산
    if(Number(number1) === ScoreSet[0]) {
        Strike++;
    } else if (Number(number1) === ScoreSet[1] || Number(number1) === ScoreSet[2]) {
        Ball++;
    }

    if(Number(number2) === ScoreSet[1]) {
        Strike++;
    } else if (Number(number2) === ScoreSet[0] || Number(number2) === ScoreSet[2]) {
        Ball++;
    }

    if(Number(number3) === ScoreSet[2]) {
        Strike++;
    } else if (Number(number3) === ScoreSet[0] || Number(number3) === ScoreSet[1]) {
        Ball++;
    }

    console.log("Strike:", Strike);
    console.log("Ball:", Ball);

    // 결과 추가
    const resultElement = createResultElement([number1, number2, number3], Strike, Ball);
    document.querySelector('.result-display').appendChild(resultElement);

    /*
    <div class="game-result">
            <img src="" id="game-result-img">
        </div>
    */
    if(Strike === 3) {
        let changeImage = document.getElementById('game-result-img');
        changeImage.src = './success.png';

        let submitButton = document.querySelector('.submit-button');
        submitButton.disabled = true;
    } else if (attemptSpan === 1) {
        let changeImage = document.getElementById('game-result-img');
        attemptSpan--;
        updateAttempts(attemptSpan);
        changeImage.src = './fail.png';

        let submitButton = document.querySelector('.submit-button');
        submitButton.disabled = true;
    } else {
        attemptSpan--;
        updateAttempts(attemptSpan);
    }

    document.getElementById('number1').value = '';
    document.getElementById('number2').value = '';
    document.getElementById('number3').value = '';

    value1 = "";
    value2 = "";
    value3 = "";

    /*
    <div class="remaining-attempts">
            남은 횟수: <span id="attempts">${attempts}</span>
        </div>
    */

    // 스트라이크와 볼 초기화
    Strike = 0;
    Ball = 0;
});