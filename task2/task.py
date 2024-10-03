def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            
            for line in file:
                cat_id, name, age = line.strip().split(',')
                
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                
                cats.append(cat_info)
            
            return cats
    
    except FileNotFoundError:
        print("Файл не знайдено")
        return []
    
    except Exception as e:
        print(e)
        return []

cats_info = get_cats_info("task2/cats.txt")
print(cats_info)
