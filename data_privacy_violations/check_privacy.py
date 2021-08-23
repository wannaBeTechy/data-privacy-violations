# -*- coding: utf-8 -*-
from rake import Rake
import nltk
from commonregex import CommonRegex
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
def check(text):
    count = 0
    if len(CommonRegex.dates(text)) > 0:
        print(CommonRegex.dates(text))
        count += 1
    if len(CommonRegex.times(text)) > 0:
        print(CommonRegex.times(text))
        count += 1
    if len(CommonRegex.phones(text)) > 0:
        print(CommonRegex.phones(text))
        count += 1
    if len(CommonRegex.links(text)) > 0:
        print(CommonRegex.links(text))
        count += 1
    if len(CommonRegex.emails(text)) > 0:
        print(CommonRegex.emails(text))
        count += 1
    if len( CommonRegex.credit_cards(text)) > 0:
        print(CommonRegex.credit_cards(text))
        count += 1
    if len(CommonRegex.street_addresses(text)) > 0:
        print(CommonRegex.street_addresses(text))
        count += 1
    if len(CommonRegex.zip_codes(text)) > 0:
        print(CommonRegex.zip_codes(text))
        count += 1
    if count > 0 :
        return True
    else:
        return False

if __name__ == '__main__':
    check("Barack Obama was born in Hawaii.my contact number is 8499839022  He was elected president in 1st july 2008.")
   