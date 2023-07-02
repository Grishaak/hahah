class RomanNumerals:

    @staticmethod
    def from_roman(roman_num: str) -> int:
        my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        for i in range(len(roman_num) - 1):
            if roman_num[i] in my_dict.keys():
                if my_dict.get(roman_num[i]) < my_dict.get(roman_num[i + 1]):
                    count -= my_dict.get(roman_num[i])
                else:
                    count += my_dict.get(roman_num[i])
        count += my_dict.get(roman_num[-1])
        return count

    @staticmethod
    def to_roman(number: int):
        if number < 1:
            return ""
        if number >= 1000:
            return "M" + RomanNumerals.to_roman(number - 1000)
        if number >= 900:
            return "CM" + RomanNumerals.to_roman(number - 900)
        if number >= 500:
            return "D" + RomanNumerals.to_roman(number - 500)
        if number >= 400:
            return "CD" + RomanNumerals.to_roman(number - 400)
        if number >= 100:
            return "C" + RomanNumerals.to_roman(number - 100)
        if number >= 90:
            return "XC" + RomanNumerals.to_roman(number - 90)
        if number >= 50:
            return "L" + RomanNumerals.to_roman(number - 50)
        if number >= 40:
            return "XL" + RomanNumerals.to_roman(number - 40)
        if number >= 10:
            return "X" + RomanNumerals.to_roman(number - 10)
        if number >= 9:
            return "IX" + RomanNumerals.to_roman(number - 9)
        if number >= 5:
            return "V" + RomanNumerals.to_roman(number - 5)
        if number >= 4:
            return "IV" + RomanNumerals.to_roman(number - 4)
        if number >= 1:
            return "I" + RomanNumerals.to_roman(number - 1)


value = 1000
roman_number = "MMDXXIV"
print(RomanNumerals.from_roman(roman_number))
print(RomanNumerals.to_roman(value))
