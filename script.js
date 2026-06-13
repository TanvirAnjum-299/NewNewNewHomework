function showInputs() {
    const shape = document.getElementById("shape").value;
    const inputs = document.getElementById("inputs");

    if (shape === "square") {
        inputs.innerHTML = `
            <input type="number" id="side" placeholder="Side Length">
        `;
    } else if (shape === "rectangle") {
        inputs.innerHTML = `
            <input type="number" id="length" placeholder="Length"><br>
            <input type="number" id="width" placeholder="Width">
        `;
    } else if (shape === "triangle") {
        inputs.innerHTML = `
            <input type="number" id="side1" placeholder="Side 1"><br>
            <input type="number" id="side2" placeholder="Side 2"><br>
            <input type="number" id="side3" placeholder="Side 3">
        `;
    }
}

function calculatePerimeter() {
    const shape = document.getElementById("shape").value;
    let perimeter = 0;

    if (shape === "square") {
        const side = Number(document.getElementById("side").value);
        perimeter = 4 * side;
    } else if (shape === "rectangle") {
        const length = Number(document.getElementById("length").value);
        const width = Number(document.getElementById("width").value);
        perimeter = 2 * (length + width);
    } else if (shape === "triangle") {
        const side1 = Number(document.getElementById("side1").value);
        const side2 = Number(document.getElementById("side2").value);
        const side3 = Number(document.getElementById("side3").value);
        perimeter = side1 + side2 + side3;
    }

    document.getElementById("result").textContent =
        `Perimeter: ${perimeter}`;
}

// Show square inputs when page loads
showInputs();