powershell -Command "Invoke-WebRequest https://github.com/Crain-32/Multiworld_Client/archive/refs/heads/master.zip -OutFile Multiworld_Client.zip"
powershell -Command "Expand-Archive Multiworld_Client.zip -DestinationPath ./"
powershell -Command "python -m pip install -r ./Multiworld_Client-master/requirements.txt"