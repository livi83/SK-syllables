import re
class Syllables:
    """
        Separating word to syllables
    """
    separator = '-'
    
    def distinguish(self, word):
        word = word.lower()
        consonants = r'bcčdďfghjklmnňpqrřsštťvwxzž'
        word = re.sub('[aeiyouáéíýóú]', 'V',word)
        word = re.sub('ch', 'c0',word)
        word = re.sub('rr', 'r0',word)
        word = re.sub('ll', 'l0',word)
        word = re.sub('nn', 'n0',word)
        word = re.sub('th', 't0',word)
        word = re.sub('[ao]u', r'0u',word)
        word = re.sub('[ao]i', '0V',word)
        word = re.sub('([^V])([rl])(0*[^0Vrl]|$)', r'\1V\3',word)
        word = re.sub('s[pt]', 's0',word)
        word = re.sub('s(tr|kv)', r's00',word)
        word = re.sub('zd', 'z0',word)
        word = re.sub('([^V0]0*)sk', r'\g<1>s0',word)
        word = re.sub('([^V0]0*)št', r'\g<1>š0',word)
        word = re.sub('[' + consonants + ']', 'K',word)
    
        return word

    def cut_mask(self, mask):
        mask = re.sub(r'(^0*V)(K0*V)', r'\1/\2',mask)
        mask = re.sub(r'(^0*V0*K0*)K', r'\1/K',mask)
        mask = re.sub(r'(K0*V(K0*$)?)', r'\1/',mask)
        mask = re.sub(r'/(K0*)K', r'\1/K',mask)
        mask = re.sub(r'/(0*V)(0*K0*V)', r'/\1/\2',mask)
        mask = re.sub(r'/(0*V0*K0*)K', r'/\1/K',mask)
        
        return mask


    def get_syllables(self, word:str):
      
        mask = self.cut_mask(self.distinguish(word))
        if mask[-1] == '/': 
            mask = mask[:-1]
        result = ''
        j = 0
        for i in mask:
            if i != '/':
                result = result + word[j]
                j += 1
            else:
                result = result + self.separator
        syllables_c = result.count('-')+1;
        return result,syllables_c