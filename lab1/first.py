from datetime import datetime

name = "Данило"
location = "Львів"
activity = "програмувати"

# Отримуємо поточний час у форматі "день.місяць.рік години:хвилини"
current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

print(f"{name} почав {activity} {current_time}. {location} — чудове місто!")
