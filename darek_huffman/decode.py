from darek_huffman.util import get_key

def decode(ciphertext,code):
    dict_from_file=code
    keys_dict=list(dict_from_file.keys())
    values_dict=list(dict_from_file.values())

    sum_string=""
    result=""
    code=ciphertext
    
    for x in code:
        sum_string+=x
        for i in values_dict:
            if (sum_string == i):
                key=get_key(i,dict_from_file)
                result+=key
                sum_string=""

    return result
