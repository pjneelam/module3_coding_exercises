#Source: Szabo, G. (2018) Create your own interactive shell with cmd in Python. 
#Available from: https://code-maven.com/interactive-shell-with-cmd-in-python
#subclass the Cmd class, so that's what we do here, though as being a skeleton we don't do anything else with it
from cmd import Cmd
#create an instance object of the MyPrompt class and immediately call the cmdloop method
class MyPrompt(Cmd):
    prompt = 'pb> '
    intro = "Welcome! Type ? to list commands"
#add commands to the system by implementing the corresponding do_* methods
    def do_exit(self, inp):
        print("Bye")
        return True
    
    def help_exit(self):
        print('exit the application. Shorthand: x q Ctrl-D.')
 
    def do_add(self, inp):
        x=int(input("Enter a number:"))
        y=int(input("Enter another number:"))
        print(x + y)
              
        #print("adding '{}'".format(inp))
 
    def help_add(self):
        print("Add a new entry to the system.")
        

    def default(self, inp):
        if inp == 'x' or inp == 'q':
            return self.do_exit(inp)
 
        print("Default: {}".format(inp))
 
    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    MyPrompt().cmdloop()