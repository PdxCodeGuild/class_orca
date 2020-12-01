// This is lab 2a of javascript where I am converting lab 15 from python to java script

// def number_to_word (x):
//         x = int(x)
//         teens = {10:"ten",
//         11:"eleven",
//         12:"twelve", 
//         13:"thirteen",
//         14:"fourteen",
//         15:"fifteen",
//         16:"sixteen",
//         17:"seventeen",
//         18:"eightteen",
//         19:"nineteen"}
//         first_digit = {1:"ten",
//         2:"twenty",
//         3:"thirty",
//         4:"forty",
//         5:"fifty",
//         6:"sixty",
//         7:"seventy",
//         8:"eighty",
//         9:"ninety"}
//         second_digit = {0:"zero",
//         1:"one",
//         2:"two",
//         3:"three",
//         4:"four",
//         5:"five",
//         6:"six",
//         7:"seven",
//         8:"eight",
//         9:"nine",
//         10:"ten"}
        
//         if 100 <= x <= 999:

//             if 1 <= x // 100 <= 9 and x % 100 == 0:
//                 return f"{second_digit[(x//100)]}-hundred"
//             elif ((x % 100)) % 10 == 0:
//                 return f"{second_digit[(x//100)]}-hundred and {first_digit[((x % 100) // 10)]}"
//             elif 1<= (x % 100) <= 9:
//                 return f"{second_digit[(x//100)]}-hundred and {second_digit[(x % 100)]}" 
//             elif 11<= (x % 100) <= 19:
//                 return f"{second_digit[(x//100)]}-hundred and {teens[(x % 100)]}" 
//             else:
//                 return f"{second_digit[(x//100)]}-hundred {first_digit[((x%100)//10)]}-{second_digit[((x%100)%10)]}"
        
//         if x == 0:
//             return second_digit[0]
//         if x // 10 == 0:
//             return second_digit[x]
//         if x == 10:
//             return teens[10]
//         if 11<= x <= 19:
//             return teens[x]
//         if 20 <= x <= 99:
//             return f"{first_digit[(x//10)]}-{second_digit[(x%10)]}" 
        
//     x = input("enter a number between 0 and 999:\n")
//     while int(x) not in range(0,1000):
//         print("No good. Try again...:\n")
//         x = input("Enter a number between 0 and 999\n")
//     print(f"{x} is {number_to_word(x)}!")

// main()

function number_to_word (y) {
       let x = parseInt(y)
    
       let teens = {10:"ten",
        11:"eleven",
        12:"twelve", 
        13:"thirteen",
        14:"fourteen",
        15:"fifteen",
        16:"sixteen",
        17:"seventeen",
        18:"eightteen",
        19:"nineteen"}
    let first_digit = {1:"ten",
        2:"twenty",
        3:"thirty",
        4:"forty",
        5:"fifty",
        6:"sixty",
        7:"seventy",
        8:"eighty",
        9:"ninety"}
    let second_digit = {0:"zero",
        1:"one",
        2:"two",
        3:"three",
        4:"four",
        5:"five",
        6:"six",
        7:"seven",
        8:"eight",
        9:"nine",
        10:"ten"}
    
    if (100 <= x && x <= 999){
        if (1 <= (Math.floor(x / 100)) <= 9 && x % 100 === 0){
                return `${second_digit[(Math.floor(x / 100))]}-hundred`
        }else if ((x % 100) % 10 === 0){
                return `${second_digit[(Math.floor(x / 100))]}-hundred and ${first_digit[Math.floor((x % 100) / 10)]}`
        }else if (1<= (x % 100) <= 9){
                return `${second_digit[(Math.floor(x / 100))]}-hundred and ${second_digit[(x % 100)]}`
        }else if (11<= (x % 100) <= 19){
                return `${second_digit[(Math.floor(x / 100))]}-hundred and ${teens[(x % 100)]}`
        } else{
                return `${second_digit[(Math.floor(x / 100))]}-hundred ${first_digit[Math.floor((x % 100) / 10)]}-${second_digit[((x % 100) % 10)]}`
        }
    };

    if (x === 0){
        return second_digit[0]
    };
    if (Math.floor(x / 10) === 0){
        return second_digit[x]
    };
    if (x === 10){
        return teens[10]
    };
    if (11<= x && x <= 19){
       return teens[x]
    };
    if (20 <= x && x <= 99){
       return `${first_digit[(Math.floor(x / 10))]}-${second_digit[(x % 10)]}`
    };
    
}


do {
   var y = prompt ("enter a number between 0 and 999:\n")
}
while (0 > parseInt(y) || parseInt(y) > 1000);
        
alert(`${y} is ${number_to_word(y)}!`)