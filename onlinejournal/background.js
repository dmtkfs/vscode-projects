function saveToFile(filename, content) {
    console.log(`Preparing to save file: ${filename}`);
    browser.runtime.sendNativeMessage('com.onlinejournal', { filename, content }, response => {
        if (response) {
            console.log(`Received response: ${JSON.stringify(response)}`);
            if (response.success) {
                console.log(`File saved successfully: ${filename}`);
            } else {
                console.error(`Failed to save file: ${filename}`);
            }
        } else {
            console.error(`No response received for file: ${filename}`);
        }
    });
}

browser.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.filename && message.content) {
        console.log(`Received message to save file: ${message.filename}`);
        saveToFile(message.filename, message.content);
    } else {
        console.error('Received message missing filename or content');
    }
});
