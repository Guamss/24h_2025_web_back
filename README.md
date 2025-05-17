# Template FastAPI

## Pour installer le projet
```
python -m venv .venv 
```
Sur Linux
```
source .venv/bin/activate
```
Sur Windows
```
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```

## Lancer le projet
```
fastapi dev src/main.py
```

## Déployer le projet 
```
docker build -t <image-name> .
docker run -d --name <container-name> -p 80:80 <image-name>
```