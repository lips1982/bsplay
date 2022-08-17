function getRandomName() {
    let n = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"],
        t = ["a", "e", "i", "o", "u"],
        r = getRandomInt(5, 7, true),
        o = "",
        i = true;
    for (; o.length < r;) i ? (o += n[getRandomInt(0, n.length - 1)], i = false) : (o += t[getRandomInt(0, t.length - 1)], i = true);
    const a = 10 - r;
    return o + getRandomInt(Math.pow(10, a - 1), Math.pow(10, a))
}
function getRandomInt(n, t, r = false) {
    const o = r ? 1 : 0;
    return Math.floor(Math.random() * (t - n + o)) + n
}

getRandomName()