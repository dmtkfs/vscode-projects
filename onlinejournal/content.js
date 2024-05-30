document.addEventListener('DOMContentLoaded', function () {
    const blacklist = ["example.com"];
    const url = window.location.hostname;

    if (blacklist.some(domain => url.includes(domain))) {
        console.log('This domain is blacklisted.');
        return;
    }

    if (browser.extension.inIncognitoContext) {
        console.log('Extension does not work in private windows.');
        return;
    }

    fetch(document.location.href)
        .then(response => response.text())
        .then(text => {
            const timestamp = new Date().toISOString().replace(/[:.-]/g, '');
            const filename = `Archived_${timestamp}.txt`;
            console.log(`Sending message to save file: ${filename}`);
            browser.runtime.sendMessage({ filename: filename, content: text }, response => {
                if (response) {
                    console.log(`Response from background: ${JSON.stringify(response)}`);
                } else {
                    console.error('No response from background script.');
                }
            });
        }).catch(error => {
            console.error(`Failed to fetch page content: ${error}`);
        });
});
