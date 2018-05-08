import re

"""result = re.match(r'AV', 'AV Analytics Vidhya AV')
print(result.group(0))


result = re.match(r'AV', 'AV Analytics Vidhya AV')
print (result.start())
print (result.end())

#Search
result = re.search(r'Analytics', 'AV Analytics Analytics Analytics Vidhya AV')
print (result)

#Findall
result = re.findall(r'Analytics', 'AV Analytics Analytics Analytics Vidhya AV')
print (result)

#Splits
result=re.split(r'y','Analytics')
print(result)

#Sub
result=re.sub(r'India','the World','AV is largest Analytics community of India')
print(result)

#compile
pattern=re.compile('AV')
result=pattern.findall('AV Analytics Vidhya AV')
print (result)
result2=pattern.findall('AV is largest analytics community of India')
print (result2)
"""
#Return the first word of a given string
result=re.findall(r'.','AV is largest Analytics community of India')
print (". is : ", result)
"""
result=re.findall(r'\w*','AV is largest Analytics community of India')
print (result)

#Extract each word (using “^“)
result=re.findall(r'^\w+','AV is largest Analytics community of India')
print (result)

result=re.findall(r'\w+$','AV is largest Analytics community of India')
print (result)

#Return the first two character of each word
result=re.findall(r'\w\w','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\b\w.','AV is largest Analytics community of India')
print (result)

#Return the domain type of given email-ids
result=re.findall(r'@\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz') 
print ("Domain name is ",result)
result=re.findall(r'@\w+.\w+','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

#Extract only domain name using “( )”
result=re.findall(r'@\w+.(\w+)','abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
print (result)

#Return date from given string
result=re.findall(r'\d{2}-\d{2}-\d{4}','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

result=re.findall(r'\d{2}-\d{2}-(\d{4})','Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
print (result)

#Return all words of a string those starts with vowel
result=re.findall(r'\w+','AV is largest Analytics community of India')
print (result)
result=re.findall(r'[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result)
result=re.findall(r'\b[aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result)

result=re.findall(r'\b[^aeiouAEIOU]\w+','AV is largest Analytics community of India')
print (result)

#Validate a phone number (phone number must be of 10 digits and starts with 8 or 9)
li=['9999999999','999999-999','99999x9999']
for val in li:
 if re.match(r'[8-9]{1}[0-9]{9}',val) and len(val) == 10:
     print ('yes')
 else:
     print ('no')
#Split a string with multiple delimiters
line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
result= re.split(r'[;,\s]', line)
print (result)

"""
