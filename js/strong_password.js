function minimumNumber(n, password) {
    const p = password; let falts = 0;
    if(!/[!@#$%^&*()+-]/.test(p)) falts++;
    if(!/[0-9]/.test(p)) falts++;
    if(p == p.toUpperCase()) falts++;
    if(p == p.toLowerCase()) falts++;
    if(n + falts < 6) falts += 6 - (falts + n);
    return falts    
}
