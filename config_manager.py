import json


def create_config(data, filename="config.json"):
    
    
    with open(filename, "w") as f: 
        
      
        json.dump(data, f, indent=4)
        
    print(f"{filename} başarıyla oluşturuldu.")


server_data = {"app": "monitor", "version": "1.0"}
create_config(server_data)