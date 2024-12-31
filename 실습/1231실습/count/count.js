const minusButton = document.getElementById('minus_button')
const plusButton = document.getElementById('plus_button')
const counter = document.getElementById('center');

minusButton.addEventListener("click", () => {
    counter.innerText = Number(counter.innerText) - 1;
});
plusButton.addEventListener("click", () => {
    counter.innerText = Number(counter.innerText) + 1;
});