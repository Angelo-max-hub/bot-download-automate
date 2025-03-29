$exclude = @("venv", "escritor.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "escritor.zip" -Force