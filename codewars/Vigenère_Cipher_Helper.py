#https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python
class VigenereCipher(object):
    def __str__(self):
        return 'class VigenereCipher'

    def __init__(self, key: str, alphabet: str) -> object:
        self.key = key
        self.alphabet = alphabet
        self.text = ''
        pass

    def key_len(self, key, text):
        while len(key) < len(text):
            key += key
        return key


    def encode(self, text):
        self.key_len(self.key, text)
        print(self.key)
        pass

    def decode(self, text):
        pass




if __name__ == '__main__':
    key = 'password'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    user = VigenereCipher(key, alphabet)
    print(user)
    #(c.encode('codewars'), 'rovwsoiv')
