"""
--------------------------------------------------------------------------------
Description: [DESCRIBE WHAT FILE DOES HERE.]

Written by [AUTHOR NAME] [<AUTHOR EMAIL HERE>], [DATE HERE]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""
import os
from fastapi import FastAPI, File, UploadFile, Header
from bioinformatics.restriction_sites import find_site
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

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


# post a file from frontend to backend?? file not working
@app.post("http://localhost:8000/files/")
async def create_file(file: bytes = File(...)):
    input_text = file.decode('UTF-8')
    # Example text: > I am a thing. \n
    # My genetic code starts right here. GCAT
    # Regular Expression Capture Groups, which are finite state machine allow for
    # the specific parsing of text.
    input_text = input_text.split("\n")[1:]
    input_text = "".join(input_text)
    removal_list = [", ", "'", "[", "]"]
    for entry in removal_list:
        input_text = input_text.replace(entry, '')
    res = find_site(
        genome_str=input_text,
    )
    print("filetest")
    return res


