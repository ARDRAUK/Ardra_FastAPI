from fastapi import FastAPI

app=FastAPI()
@app.get("/index")
def index():
    return{"name":"ardra","designation":"data sceintist"}