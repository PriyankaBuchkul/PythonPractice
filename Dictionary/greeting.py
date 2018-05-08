name_for_userid={382:"Priyanka",590:"Poonam",255:"Nayana"}

def greeting(userid):
      return "hi %s!"%name_for_userid.get(userid,"there")


print(greeting(382))
