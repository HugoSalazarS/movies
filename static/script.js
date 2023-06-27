function executeAction(actionUrl, inputElement, outputElement) {
    var inputValue = inputElement.value;
    var fullUrl = actionUrl.replace("{input}", encodeURIComponent(inputValue));
    
    fetch(fullUrl)
        .then(response => response.text())
        .then(data => {
            outputElement.value = data;
        })
        .catch(error => {
            outputElement.value = "An error occurred while executing the action.";
            console.error(error);
        });
}

function handleKeyPress(event, actionUrl, inputElement, outputElement) {
    if (event.key === "Enter") {
        executeAction(actionUrl, inputElement, outputElement);
    }
}
