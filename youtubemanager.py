RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = "\033[0;35m"
CYAN = "\033[36m"
END = "\033[0m"


def banner():
    font = f"""
      {CYAN}
                      _         _                                                         
                     | |       | |                                                        
  _   _  ___  _   _  | |_ _   _| |__   ___   _ __ ___   __ _ _ __   __ _  __ _  ___ _ __  
 | | | |/ _ \| | | | | __| | | | '_ \ / _ \ | '_ ` _ \ / _` | '_ \ / _` |/ _` |/ _ \ '__| 
 | |_| | (_) | |_| | | |_| |_| | |_) |  __/ | | | | | | (_| | | | | (_| | (_| |  __/ |    
  \__, |\___/ \__,_|  \__|\__,_|_.__/ \___| |_| |_| |_|\__,_|_| |_|\__,_|\__, |\___|_|    
   __/ |                                                                  __/ |           
  |___/                                                                  |___/            
  
     """

    print(font)


def list_all_vedios(vedios):
   pass


def add_youtube_vedio(vedios):
    pass


def update_youtube_vedio(vedios):
    pass


def delete_youtube_vedio(vedios):
    pass


def exit_app():
    pass


vedios = []
while True:
    banner()
    print("1.list al youtube vedios")
    print("2.Add a  youtube video")
    print("3.Update a youtube vedio details")
    print("4.Delete a youtube vedio")
    print("5.exit the app")
    choice = input("enter your choice")
    match choice:
        case "1":
            list_all_vedios(vedios)
        case "2":
            add_youtube_vedio(vedios)
        case "3":
            update_youtube_vedio(vedios)
        case "4":
            delete_youtube_vedio(vedios)
        case "5":
            exit_app()
