// JavaScript to handle character counter for the textarea
const textarea = document.querySelector('textarea');
const charCounter = document.querySelector('.char-counter');

textarea.addEventListener('input', () => {
    const remaining = 5000 - textarea.value.length;
    charCounter.textContent = `${remaining} chars left`;
});
