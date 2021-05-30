from fastapi import FastAPI,Request,UploadFile,File
from fastapi.templating import Jinja2Templates
import write
import os,shutil


app=FastAPI()
templates=Jinja2Templates(directory="templates")

@app.get("/")
def home(request:Request):
	return templates.TemplateResponse("index.html",{"request":request})


@app.post("/extract")
def extract(image:UploadFile=File(...)):
	temp_file=saveFile(image,path="temp",save_as="temp")
	text=write.convert(temp_file)
	return {"text":text}

def saveFile(up_file,path=".",save_as="default"):
	extension=os.path.splitext(up_file.filename)[-1]
	temp_file=os.path.join(path,save_as+extension)
	with open(temp_file,"wb") as buffer:
		shutil.copyfileobj(up_file.file,buffer)
	return temp_file



