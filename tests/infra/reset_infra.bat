docker-compose down
docker system prune -f --volumes
docker-compose up -d
Powershell.exe -executionpolicy remotesigned -File "./CheckURL.ps1"