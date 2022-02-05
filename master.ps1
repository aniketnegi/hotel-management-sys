Set-Location D:\programming\learning-flask

$venv_path = "D:\programming\learning-flask\venv"

$venv_exist = Test-Path $venv_path

$dependencies_exist = Test-Path D:\programming\learning-flask\runtime.txt

if ($venv_exist){
Write-Host "
Venv exists
"
Write-Host "
Using venv
"
Write-Host "
Activating Virtual Environemnt!...
"
.\venv\Scripts\activate
Write-Host "
VirtualEnv has been activated!
"
if ($dependencies_exist){
Write-Host "
Dependencies already Exist!
"
Write-Host "
Done!
"
} else {
Write-Host "
Installing dependencies...
"
pip install -r requirements.txt
fsutil file createnew runtime.txt 0
Write-Host "
Dependencies installed
"
Write-Host "
Done!
"
}
}
else{
Write-Host "
venv does not exist
"
Write-Host "
creating venv
"
pip install virtualenv
virtualenv --python "C:\Users\rajee\AppData\Local\Programs\Python\Python38\python.exe" venv
Write-Host "
venv created
"
Write-Host "
Using venv
"
Write-Host "
Installing dependencies...
"
.\venv\Scripts\activate
pip install -r requirements.txt
fsutil file createnew runtime.txt 0
Write-Host "
Dependencies installed
"
Write-Host "
Done
"
}


$choice = Read-Host -Prompt ("

Press 1 to run initial setup.
Press 2 to start the webserver.
Press 3 to run the ADMIN utility.
")

$i = 0

while ($i -eq 0) {
if($choice -eq 1){
Write-Host "
Creating the Database...
"
Set-Location .\init-setup
python create-database.py

Write-Host "
Populating the database with admin users and other setup data...
"
python insert-data.py
Set-Location ..
} elseif($choice -eq 2){
Write-Host "
Starting the webserver on port:5000
"
python .\app.py
$i = 1
} elseif($choice -eq 3){
Write-Host "
Running the Admin Utility...
"
Write-Host "
WITH GREAT POWER COMES GREAT RESPONSIBILITY!
"
python .\add-admins.py
$i = 1
}
}
