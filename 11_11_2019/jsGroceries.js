let groceryList = ['bacon', 'axe body spray', 'monster energy'];

for(let i = 0; i < groceryList.length; i++) {
    groceryList[i] = groceryList[i] + ' get it, son';
}

let notherList = ['1', '2', '3', '4']
let bigList = [groceryList, notherList]
console.log(bigList)
console.log('test ' + bigList[1][1])
