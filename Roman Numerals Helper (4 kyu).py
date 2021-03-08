class RomanNumerals():
    def __init__(self, n):
        self.to_roman(n)
        self.from_roman(n)

    def to_roman(n):
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        thousands = ['', 'M', 'MM', 'MMM']
        return thousands[n//1000] + hundreds[n//100%10] + tens[n//10%10] + ones[n%10]

    def from_roman(n):
        result = 0
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(n)-1):
            if nums[n[i]] < nums[n[i+1]]:
                result -= nums[n[i]]
            elif nums[n[i]] >= nums[n[i+1]]:
                result += nums[n[i]]
        result += nums[n[len(n)-1]]
        return result
