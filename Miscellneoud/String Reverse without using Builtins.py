def reverse(s):
      a=""
      for i in range(1,len(s)+1):
            a=a+s[len(s)-i]
            print(a)
      return a
print(reverse("abcde12345"))


def reverse1(text):
    rev_text = ""     
    for char in text:  
        rev_text = char + rev_text
    return rev_text

print(reverse1("hello"))


def rev(s):
      p=""
      for i in s:
            p=i+p
            print(p)
      return p

print(rev("abcde"))

