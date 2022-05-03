function minimumNumber(n: number, password: string): number {
    let result = 0;
    result += /[0-9]/.test(password) ? 0 : 1;
    result += /[a-z]/.test(password) ? 0 : 1;
    result += /[A-Z]/.test(password) ? 0 : 1;
    result += /[!@#$%^&*()+-]/.test(password) ? 0 : 1;
    if(n + result < 6) {
        result = 6 - n;
    }
    return result;
}

function minimumNumber(n, p) {
    return Math.max(6-p.length, !/[A-Z]/.test(p) + !/[a-z]/.test(p) + !/\d/.test(p) + !/[!@#$%^&*()\-+]/.test(p))
}