// Two Sum:
// - Problem Statement: Given an array of integers, find two numbers such that they add up to a specific target.

function twoSum(input, target) {
    let allSets = []
    let dataSets = {};
    for (let i = 0; i < input.length; i++) {
        let num = input[i];
        let remainingValue = target - num;
        if (remainingValue in dataSets) {
            allSets.push([input[dataSets[remainingValue]], input[i]]); // returns the values of the two numbers
        }
        dataSets[num] = i; // store the index of the current number
    }
    return allSets; // return null if no pair is found
}


  let input = [1, 4, 2, 3, 5, 7];
  let target = 5;
  console.log(twoSum(input, target));