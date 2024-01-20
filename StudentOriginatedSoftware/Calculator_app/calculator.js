// Calculator state variables
let runningTotal = 0;
let buffer = "0";
let previousOperator;
const screen = document.querySelector(".screen");

// Handles the button clicks
function buttonClick(value) {
    if (isNaN(parseInt(value))) {
        handleSymbol(value);  // Handle non-numeric symbols
    } else {
        handleNumber(value);  // Handle numeric values
    }
    rerender();  // Update the display
}

// Handles the number input
function handleNumber(value) {
    if (buffer === "0") {
        buffer = value;  // Replace initial buffer value
    } else {
        buffer += value;  // Append number to buffer
    }
}

// Handles the mathematical operations (+, -, x, ÷)
function handleMath(value) {
    if (buffer === "0") {
        return;  // Exit if buffer is zero
    }

    const intBuffer = parseInt(buffer);  // Convert buffer to integer
    if (runningTotal === 0) {
        runningTotal = intBuffer;  // Set running total if it's the first operation
    } else {
        flushOperation(intBuffer);  // Perform the pending operation
    }

    previousOperator = value;  // Store current operation

    buffer = "0";  // Reset buffer
}

// Performs the stored operation
function flushOperation(intBuffer) {
    if (previousOperator === "+") {
        runningTotal += intBuffer;
    } else if (previousOperator === "-") {
        runningTotal -= intBuffer;
    } else if (previousOperator === "x") {
        runningTotal *= intBuffer;
    } else {
        runningTotal /= intBuffer;
    }
}

// Handles special symbols: C, =, and backspace(←)
function handleSymbol(value) {
    switch (value) {
        case "C":
            buffer = "0";  // Clear buffer
            runningTotal = 0;  // Reset total
            break;
        case "=":
            if (previousOperator === null) {
                return;  // Do nothing if no operation is set
            }
            flushOperation(parseInt(buffer));  // Perform the operation
            previousOperator = null;
            buffer = "" + runningTotal;  // Update buffer with result
            runningTotal = 0;  // Reset running total
            break;
        case "←":
            if (buffer.length === 1 || (buffer.length === 2 && buffer.startsWith('-'))) {
                buffer = "0";  // Reset buffer if it's a single digit or negative single digit
            } else {
                buffer = buffer.substring(0, buffer.length - 1);  // Remove last digit
            }
            break;
        case "+":
        case "-":
        case "x":
        case "÷":
            handleMath(value);  // Handle the math operation
            break;
    }
}

// Updates the screen display
function rerender() {
    screen.innerText = buffer;  // Display the current buffer value
}

// Initialization to set up event listeners
function init() {
    document
        .querySelector(".calc-buttons")
        .addEventListener("click", function (event) {
            buttonClick(event.target.innerText);  // Handles button click events
        });
}

init();  
