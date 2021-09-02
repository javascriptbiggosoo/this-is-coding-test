function solution(arr1, arr2) {
    let answer = [];
    const hang = arr1.length
    const yul = arr1[0].length
    for (let i=0; i< hang; i++){
        let arrSum = []
        for (let j=0; j< yul; j++){
            arrSum.push(arr1[i][j] + arr2[i][j])
        }
        answer.push(arrSum)
    }

    // 행, 열 길이를 찾는다.
    // 각 칸의 값을 더한다
    // answer에 넣어준다.
    return answer;
}