from src.classes.ui import UI

if __name__ == "__main__":  
  while True:
    try:  
      ui = UI()
      ui.menu()
      key = input("press any key to continue or press 'q' to exit")
      if key == "q":
        break
      print("-" * 50)
    except Exception :
      input("Unexpected error occurred, press any key to clear the screen")