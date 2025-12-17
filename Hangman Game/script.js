// List of predefined words
const words = ["apple", "banana", "cherry", "date", "elderberry"];

// Game variables
let word = "";
let guessed = new Set();
let incorrect = 0;
const maxIncorrect = 6;

// DOM elements
const startScreen = document.getElementById("start-screen");
const gameScreen = document.getElementById("game-screen");
const endPopup = document.getElementById("end-popup");
const wordDisplay = document.getElementById("word-display");
const guessedLetters = document.getElementById("guessed-letters");
const incorrectCount = document.getElementById("incorrect-count");
const guessInput = document.getElementById("guess-input");
const guessBtn = document.getElementById("guess-btn");
const newGameBtn = document.getElementById("new-game-btn");
const startBtn = document.getElementById("start-btn");
const playAgainBtn = document.getElementById("play-again-btn");
const closePopupBtn = document.getElementById("close-popup-btn");
const popupTitle = document.getElementById("popup-title");
const popupMessage = document.getElementById("popup-message");

// Start the game from start screen
startBtn.addEventListener("click", () => {
    startScreen.classList.add("hidden");
    gameScreen.classList.remove("hidden");
    startNewGame();
});

// Start a new game
function startNewGame() {
    word = words[Math.floor(Math.random() * words.length)];
    guessed.clear();
    incorrect = 0;
    updateDisplay();
    guessInput.value = "";
    guessInput.disabled = false;
    guessBtn.disabled = false;
    endPopup.classList.add("hidden");
}

// Update the display
function updateDisplay() {
    const display = word.split("").map(c => guessed.has(c) ? c : "_").join(" ");
    wordDisplay.textContent = display;
    guessedLetters.textContent = `Guessed letters: ${Array.from(guessed).sort().join(", ")}`;
    incorrectCount.textContent = `Incorrect guesses left: ${maxIncorrect - incorrect}`;
}

// Handle guess
function makeGuess() {
    const guess = guessInput.value.toLowerCase();
    guessInput.value = "";
    
    if (guess.length !== 1 || !/[a-z]/.test(guess)) {
        alert("Please enter a single letter.");
        return;
    }
    if (guessed.has(guess)) {
        alert("You already guessed that letter.");
        return;
    }
    
    guessed.add(guess);
    if (word.includes(guess)) {
        // Good guess - no alert needed
    } else {
        incorrect++;
    }
    
    updateDisplay();
    
    // Check win/loss
    if (word.split("").every(c => guessed.has(c))) {
        showEndPopup("You Won!", `Congratulations! The word was '${word}'.`);
    } else if (incorrect >= maxIncorrect) {
        showEndPopup("You Lost!", `Better luck next time! The word was '${word}'.`);
    }
}

// Show end popup
function showEndPopup(title, message) {
    popupTitle.textContent = title;
    popupMessage.textContent = message;
    endPopup.classList.remove("hidden");
    guessInput.disabled = true;
    guessBtn.disabled = true;
}

// Event listeners
guessBtn.addEventListener("click", makeGuess);
newGameBtn.addEventListener("click", startNewGame);
playAgainBtn.addEventListener("click", () => {
    endPopup.classList.add("hidden");
    startNewGame();
});
closePopupBtn.addEventListener("click", () => {
    endPopup.classList.add("hidden");
    gameScreen.classList.add("hidden");
    startScreen.classList.remove("hidden");
});
guessInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") makeGuess();
});