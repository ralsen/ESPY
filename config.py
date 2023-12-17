import hashlib

def calcHash(data):
    # Entferne den letzten Wert aus dem Dictionary, um die Prüfsumme zu berechnen
    data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    data['hash'] = checksum
    # Setze den berechneten checksum als Wert für 'checksum' im Dictionary

def testHash(data):
    oldHash = data.pop('hash', '')
    sorted_string = ''.join(sorted(f"{key}{value}" for key, value in data.items()))
    checksum = sum(ord(char) for char in sorted_string)
    return checksum==oldHash    
