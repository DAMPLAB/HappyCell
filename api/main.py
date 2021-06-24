"""
--------------------------------------------------------------------------------
Description: [main python file of the API backend]

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.24.2021]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""

from fastapi import FastAPI, File
from bioinformatics.restriction_sites import find_site
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080"]

# --------------------------- CONSTANT DECLARATION -----------------------------
app = FastAPI()
path = "/code/HappyCell/api"

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------- STATEFUL OBJECTS -----------------------------

# ------------------------------ GENERIC UTILITY -------------------------------
@app.get("/echo/{ret_string}")
async def echo(ret_string: str):
    return {
        "message": f"{ret_string}",
    }


@app.post("/echopost/{ret_string}")
async def echopost(ret_string: str):
    return {
        "postmessage": f"{ret_string}",
    }


# how to check whether backend received from backend page?
# where Ok statusText "Ok" come from?

class StringTest(BaseModel):
    name: str


@app.post("/postStringTest/")
async def create_string(strings: StringTest):
    return strings


# post a file from frontend to backend
@app.post("/files/")
async def create_file(file: bytes = File(...)):
    input_text = file.decode('UTF-8')
    # input_text was in byte, we decode it here
    input_text = input_text.split("\n")[1:]
    input_text = "".join(input_text)
    removal_list = [", ", "'", "[", "]"]
    for entry in removal_list:
        input_text = input_text.replace(entry, '')
    res = find_site(sequence=input_text)
    print(res)
    return res
