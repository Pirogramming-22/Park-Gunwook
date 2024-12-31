const slider = document.getElementById("text_slider");
const textContainer = document.getElementById("text_container");
const texts = textContainer.children;


console.log(slider);
console.log(textContainer);
console.log(texts);

slider.addEventListener("input", (event) => {
    console.log(event.target.value);
    Array.from(texts).map((text) => {
        text.style.fontWeight = event.target.value * 10;
    });
});