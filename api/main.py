"""
--------------------------------------------------------------------------------
Description: [DESCRIBE WHAT FILE DOES HERE.]

Written by [AUTHOR NAME] [<AUTHOR EMAIL HERE>], [DATE HERE]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
# --------------------------- CONSTANT DECLARATION -----------------------------
app = FastAPI()
path = '/code/HappyCell/api'

# --------------------------- STATEFUL OBJECTS -----------------------------

# ------------------------------ GENERIC UTILITY -------------------------------
#@app.get("/echo/{ret_string}")
#async def echo(ret_string: str):
#    return {
#       "message": f"{ret_string}",
#   }
@app.get("/")
def index():
    return {"Hello":"Wooorld"}

@app.get("/Ecoli")
def Ecoli():
    return FileResponse("files/Ecoli.png")

@app.get("/sequence")
def sequence():
    return FileResponse("files/TP53_gene.gna")

