from pyautogui import moveTo, click, locateCenterOnScreen, write 
from PRKG import Prkg



class Automation:
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.SET_Location = None
        self.x = None
        self.y = None

    def find_location(self, Location):
        # If SET_Location variable is None
        # attempt to set the variable
        self.SET_Location = None
        while self.SET_Location == None:
            try:    
                self.SET_Location = locateCenterOnScreen(Location,confidence=0.8)
                print(self.SET_Location)
            except Exception as E:
                print(E)
            # If the variable != None return the variable
            if self.SET_Location != None:    
                return self.SET_Location
        
        # Else set the variable to none
        else:
            self.SET_Location = None
            
    def goto_click(self, x=False, y=False):
        if (x,y) != (False,False):
            moveTo(x,y)
            click()
        else:    
            moveTo(self.SET_Location)
            click(self.SET_Location)
        

    def automate(self):
        print("Searching for location.")
        self.SET_Location = self.find_location("C:/Users/hadaw/DDos_Experimentation/tab_location.png")
        self.goto_click()
        
        print("Searching for second location")
        self.SET_Location = self.find_location("C:/Users/hadaw/DDos_Experimentation/activate_key_location.png")
        self.goto_click()
        
        print("Generating keys")
        prkg = Prkg(1000)
        for keys in prkg.keys:
            print("Searching for search box")
            self.SET_Location = self.find_location("C:/Users/hadaw/DDos_Experimentation/select_search.png")
            self.goto_click()
            
            print("Writing keys")
            write(keys)
            print("Submiting key")
            self.SET_Location = self.find_location("C:/Users/hadaw/DDos_Experimentation/activate_button.png")
            self.goto_click()
            
        

if __name__ == "__main__":    
    auto = Automation()
    auto.automate()
