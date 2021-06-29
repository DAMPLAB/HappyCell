"""
--------------------------------------------------------------------------------
Description: [main python file of the API backend]

Written by [Beining Ouyang] [bouyang@bu.edu], [Jun.24.2021]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""

from fastapi import FastAPI, File
from bioinformatics.restriction_sites import (
    find_site,
    format_fasta_file,
    calculate_length_of_plasmid,
)
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
    global res
    res = find_site(sequence=input_text)
    return res


@app.post("/display_plasmid/")
async def create_plasmid_struct(file: bytes = File(...)):
    name, sequence = format_fasta_file(file)
    sequence_length = calculate_length_of_plasmid(sequence)
    sites = find_site(sequence)
    return {
        "sequence_name": name,
        "sequence_length": sequence_length,
        "restriction_sites": sites,
        "basepair_name": f'{sequence_length} bp'
    }


# post a file from frontend to backend ???
# question: is this the right way to return dropzone data to frond end
@app.get("/files_return/")
async def return_sites():
    print(res)
    return {"return": f"{res}"}
