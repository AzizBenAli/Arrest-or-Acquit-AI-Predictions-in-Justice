from pydantic import BaseModel
from fastapi import FastAPI, Form
class BankNote(BaseModel):
    driver_gender: str= Form(...)   
    driver_age: float= Form(...)
    driver_race_raw: str   = Form(...)
    driver_race: str= Form(...)
    violation: str= Form(...)
    search_type: str= Form(...)
    contraband_found: bool= Form(...)
    search_basis: str= Form(...)
    year: int = Form(...)
    month: int = Form(...)
    day_of_week: int= Form(...)


 