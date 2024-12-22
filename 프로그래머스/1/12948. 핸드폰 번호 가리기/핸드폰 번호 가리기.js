function solution(phone_number) {
    let a = phone_number.length;
    return '*'.repeat(a - 4) + phone_number.slice(a - 4);
}