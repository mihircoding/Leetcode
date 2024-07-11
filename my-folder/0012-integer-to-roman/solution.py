class Solution:
    def intToRoman(self, num: int) -> str:
        sub = {
            4 : 'IV',
            9 : 'IX',
            40 : 'XL',
            90 : 'XC',
            400: 'CD',
            900: 'CM'
        }
        placement = {
            4 : 'M',
            3 : 'C',
            2 : 'X',
            1 : 'I'
        }
        fives = {
            3 : 'D',
            2 : 'L',
            1 : 'V'
        }
        ans = ''
        number = [int(x) for x in str(num)]
        for i in range(len(number)):
            place = len(number) - i
            if number[i] != 4 and number[i] != 9:
                digit = number[i]
                if digit >= 5:
                    ans += fives[place]
                    digit -= 5
                ans += (placement[place] * digit)
            else:
                ans += sub[number[i] * ( 10**(place-1) )]
        return ans
