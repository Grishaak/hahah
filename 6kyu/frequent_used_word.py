message = "'dctOER,!'dctOER_?!!;cBtW.,;cBtW KfJcEMIeE?/!:/'dctOER?cBtW;;- KfJcEMIeE.! ,,cBtW._cBtW_?;'dctOER;--_KfJcEMIeE ,KfJcEMIeE!/ ,KfJcEMIeE?,_'dctOER/:cBtW..KfJcEMIeE-?!cBtW; cBtW!;-._KfJcEMIeE.??cBtW-.!:cBtW?.cBtW/.cBtW_,;cBtW!,!cBtW:cBtW.;.cBtW,/KfJcEMIeE--_cBtW;:?.?cBtW,;cBtW:_:'dctOER:,;"
from string import punctuation


def top_3_words(text):
    text = text.lower()
    for char in punctuation:
        if char != "'":
            text = text.replace(char, " ")
    new_text = []
    text = text.split()
    for _ in range(len(text)):
        lent = len(text[_])
        if text[_] != ("'" * lent):
            new_text.append(text[_])
    sds = []
    new_dict = {}
    for item in new_text:
        new_dict[item] = text.count(item)
    print(sds)
    new_list = []
    new_text = []
    second_dict = {}
    for _ in new_dict.items():
        new_list.append(_)
    for i in range(len(new_list)):
        maximum = max(new_dict.values())
        need_value = list(new_dict.keys())[list(new_dict.values()).index(maximum)]
        new_text.append(need_value)
        second_dict[need_value] = new_dict.pop(need_value)
    new_text = new_text[:3]
    return new_text


# top_3_words(message)
print(top_3_words(message))

# mydict = {'george': 16, 'amber': 19}
# print(list(mydict.keys())[list(mydict.values()).index(max(mydict.values()))])
