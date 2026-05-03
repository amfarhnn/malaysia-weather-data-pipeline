from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from src.config import Config

app = FastAPI(
    title="Malaysia Weather Data API",
    description="API for accessing processed Malaysia weather data from PostgreSQL",
    version="1.0.0"
)

engine = create_engine(Config.POSTGRES_URL)


@app.get("/")
def root():
    return {
        "message": "Malaysia Weather Data API",
        "endpoints": [
            "/weather/latest",
            "/weather/city/{city}",
            "/weather/summary"
        ]
    }


@app.get("/weather/latest")
def get_latest_weather():
    query = text("""
        SELECT city, temperature_c, humidity_percent, precipitation_mm,
               wind_speed_kmh, weather_time, rain_status
        FROM weather_observations
        ORDER BY weather_time DESC
        LIMIT 10;
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        rows = [dict(row._mapping) for row in result]

    return {"data": rows}


@app.get("/weather/city/{city}")
def get_weather_by_city(city: str):
    query = text("""
        SELECT city, temperature_c, humidity_percent, precipitation_mm,
               wind_speed_kmh, weather_time, rain_status
        FROM weather_observations
        WHERE LOWER(city) = LOWER(:city)
        ORDER BY weather_time DESC
        LIMIT 10;
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"city": city})
        rows = [dict(row._mapping) for row in result]

    if not rows:
        raise HTTPException(status_code=404, detail="City not found")

    return {"city": city, "data": rows}


@app.get("/weather/summary")
def get_weather_summary():
    query = text("""
        SELECT 
            city,
            ROUND(AVG(temperature_c)::numeric, 2) AS avg_temperature,
            ROUND(AVG(humidity_percent)::numeric, 2) AS avg_humidity,
            COUNT(*) AS total_records
        FROM weather_observations
        GROUP BY city
        ORDER BY city;
    """)

    with engine.connect() as conn:
        result = conn.execute(query)
        rows = [dict(row._mapping) for row in result]

    return {"summary": rows}
