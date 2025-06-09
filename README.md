# settr
automates setting desktop similar to windows spotlight

Enter the path of whatever folder you'd like and this script will filter out the extensions (eg. .jpg, .png) and set your wallpaper to a random one in the folder, it will also check to make sure it is not setting the same as the current wallpaper.
Also, I've included a sample wallpaper folder.


To automate this for daily use, use the Windows "Task Scheduler" and create a Basic Task.

![image](https://github.com/user-attachments/assets/790c00a5-b74f-4efe-ab36-6dc2af53c91f)

When creating the task I found it works better if you set the "Program/script" to your python.exe and set the settr.py file as an argument.

![image](https://github.com/user-attachments/assets/09ffd390-34a4-40fc-8223-cf203e9b20d2)

I recommend checking "Run task as soon as possible after a scheduled start is missed" in the task properties.

![image](https://github.com/user-attachments/assets/0c0f701d-6291-4bb8-b915-53100116e7e8)
