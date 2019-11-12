// let groceryList = ['bacon', 'axe body spray', 'monster energy'];

// for(let i = 0; i < groceryList.length; i++) {
//     groceryList[i] = groceryList[i] + ' get it, son';
// }

// let notherList = ['1', '2', '3', '4']
// let bigList = [groceryList, notherList]
// console.log(bigList)
// console.log('test ' + bigList[1][1])
arr1 = [[1, 3], 
        [2, 4]];

arr2 = [[5, 2], 
        [1, 0]]

function matrixAdd(a, b) {
    let result = []
    for(let i = 0; i < a.length; i++){
        result.push([])
        for(let j = 0; j < i.length; j++){
            result[i].push(a[i][j] + b[i][j])
        }
    } console.log(result)
}