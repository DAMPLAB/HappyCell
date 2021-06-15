"""
--------------------------------------------------------------------------------
Description: [DESCRIBE WHAT FILE DOES HERE.]

Written by [AUTHOR NAME] [<AUTHOR EMAIL HERE>], [DATE HERE]
[PROJECT LICENCSE HERE]
--------------------------------------------------------------------------------
"""
import os
from fastapi import FastAPI
from bioinformatics.restriction_sites import get_restriction_sites
from fastapi.middleware.cors import CORSMiddleware

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
