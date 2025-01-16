from pydantic import BaseModel, Field

class Data(BaseModel):
    PM2_5: float = Field(..., alias='PM2.5')
    PM10: float = Field(..., alias='PM10')
    NO: float = Field(..., alias='NO')
    NO2: float = Field(..., alias='NO2')
    O3: float = Field(..., alias='O3')
    SO2: float = Field(..., alias='SO2')
    
