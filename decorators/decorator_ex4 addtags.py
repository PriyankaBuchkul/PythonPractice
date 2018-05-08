def Addtags(*tags):
      def decorator(oldfunc):
            def inside(*args,**kwargs):
                  code=oldfunc(*args,**kwargs)
                  for tag in reversed(tags):
                        code="<{0}>{1}</{0}>".format(tag,code)
                        print("Tag is ",tag)
                  return code
            return inside
      return decorator


@Addtags("p","i","b")
def MyWebWelcome(name):
      return "Welcome " + name+"  To My blog"

print(MyWebWelcome("Priya"))
          
        
