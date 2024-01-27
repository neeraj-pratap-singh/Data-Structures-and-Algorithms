// Two Sum:
// - Problem Statement: Given an array of integers, find two numbers such that they add up to a specific target.

function twoSum(input, target) {
    let dataSets = {};
    for (let i = 0; i < input.length; i++) {
        let num = input[i];
        let remainingValue = target - num;
        if (remainingValue in dataSets) {
            return [input[dataSets[remainingValue]], input[i]]; // returns the indices of the two numbers
        }
        dataSets[num] = i; // store the index of the current number
    }
    return null; // return null if no pair is found
}


  let input = [1, 4, 2, 2, 5, 7];
  let target = 5;
  console.log(twoSum(input, target));