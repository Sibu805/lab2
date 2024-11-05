import xml.etree.ElementTree as ET

def operation(file):
    
    tree = ET.parse(file)
    root = tree.getroot()
    
    num_codes = []
    char_codes = []
    
    for currency in root.findall('Valute'):
        num_code = currency.find('NumCode').text
        char_code = currency.find('CharCode').text
        
        if num_code is not None:
            num_codes.append(int(num_code))  
        if char_code is not None:
            char_codes.append(char_code)    
    
    return num_codes, char_codes

file = 'currency.xml'
num_codes, char_codes = operation(file)

print("NumCode List:", num_codes)
print("CharCode List:", char_codes)
