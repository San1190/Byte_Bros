

function isValidIP(str) {
    let arr = str.split('.');
    if (arr.length !== 4) return false;
    for (let i = 0; i < arr.length; i++) {
        if (arr[i].length === 0 || arr[i].length > 3) return false;
        if (arr[i].length > 1 && arr[i][0] === '0') return false;
        if (arr[i].match(/[^0-9]/) || +arr[i] > 255) return false;
    }
    return true;
}   