import json


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


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(vedios):
    with open("youtube.txt", "w") as file:
        json.dump(vedios, file)


def list_all_vedios(vedios):
    for index, val in enumerate(vedios):
        print(f"{index}.")
        print(f"{val}")


def add_youtube_vedio(vedios):
    nameV = input("enter a name of vedio")
    time = input("enter a timing of vedio")
    vedios.append({"name": nameV, "time": time})
    save_data_helper(vedios)


def update_youtube_vedio(vedios):
    pass


def delete_youtube_vedio(vedios):
    pass


def exit_app():
    pass


def main():
    vedios = load_data()
    while True:
        banner()
        print("1.list al youtube vedios")
        print("2.Add a  youtube video")
        print("3.Update a youtube vedio details")
        print("4.Delete a youtube vedio")
        print("5.exit the app")
        choice = int(input("enter your choice"))
        match choice:
            case 1:
                list_all_vedios(vedios)
            case 2:
                add_youtube_vedio(vedios)
            case 3:
                update_youtube_vedio(vedios)
            case 4:
                delete_youtube_vedio(vedios)
            case 5:
                break
            case _:
                print("invalid choice")


if __name__ == "__main__":
    main()
