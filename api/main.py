"""
--------------------------------------------------------------------------------
Description: [DESCRIBE WHAT FILE DOES HERE.]

Written by [AUTHOR NAME] [<AUTHOR EMAIL HERE>], [DATE HERE]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""
import os
from fastapi import FastAPI, File, UploadFile, Header
from bioinformatics.restriction_sites import get_restriction_sites
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


@app.get("/find_restriction_site/{fasta_site_file}/{restriction_site_file}")
async def find_restriction_sites(fasta_site_file: str, restriction_site_file: str):
    file_root = os.path.join(os.getcwd(), 'files')
    res = get_restriction_sites(
        genome_fp=os.path.join(file_root, fasta_site_file),
        restriction_fp=os.path.join(file_root, restriction_site_file),
    )
    return {
        "restriction_sites": res,
    }


@app.post("/echopost/{ret_string}")
async def echopost(ret_string: str):
    return {
        "postmessage": f"{ret_string}",
    }
# how to check whether backend received from backend page?
# where Ok statuText "Ok" come from?

class StringTest(BaseModel):
    name: str

@app.post("/postStringTest/")
async def create_string(strings: StringTest):
    return strings


