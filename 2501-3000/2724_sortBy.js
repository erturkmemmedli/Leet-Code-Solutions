/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    arr = arr.sort((a, b) => fn(a) - fn(b))
    return arr;
};
