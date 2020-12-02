// # iterate through a list of data
// data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
let data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9];
let peaks_list = [];

// # when value is lower on both sides = peak
// def peaks(data):
//     peaks_list = []
//     for i in range(1, len(data)-1):
//         if data[i + 1] < data[i] > data[i-1]:
//             peaks_list.append(i)
console.log(data.length)
function peak(data) {
    last = data.length;
    for (let i=0; i < last; i++) {
        if (data[i + 1] < data[i] > data[i-1]){
            peaks_list.push([i]);
        }
    }
//     last = data.length-1;
//     i = 0;
//     while (i < last && data[i] > data[i + 1]){
//         peaks_list.push(i);
//         i++;
//     }
};
peak(data)
console.log(peaks_list)


            
//     print(peaks_list)
// # when value is higher on both sides, valley
// def valleys(data):
//     valleys_list = []
//     for i in range(1, len(data)-1):
//         if data[i + 1] > data[i] < data[i - 1]:
//             valleys_list.append(i)
        
//     print(valleys_list)
// # assign peaks and valleys into seperate list in the order they occur
// def peaks_and_valleys(data):
//     p_v_list = []
//     for i in range(1, (len(data)-1)):
//         if data[i + 1] < data[i] > data[i-1]:
//             p_v_list.append(i)
//         elif data[i + 1] > data[i] < data[i - 1]:
//             p_v_list.append(i)
//     print(p_v_list)
    






// peaks(data)
// valleys(data)
// peaks_and_valleys(data)