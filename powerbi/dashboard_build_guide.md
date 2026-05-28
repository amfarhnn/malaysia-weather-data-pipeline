# Power BI Dashboard Build Guide

This guide builds a recruiter-ready Power BI dashboard for the Malaysia Weather Data Engineering Pipeline.

## Recommended Data Source

Use PostgreSQL for the final dashboard because the pipeline appends records to the `weather_observations` table. Azure Blob Storage remains the data lake layer for raw and processed CSV history.

Use CSV only for a quick static mockup:

```text
data/processed/weather_cleaned.csv
```

Use PostgreSQL for the portfolio dashboard:

```text
weather_observations
```

## Import Data

1. Open Power BI Desktop.
2. Select `Home > Get data > PostgreSQL database`.
3. Enter the PostgreSQL server and database from `.env`.
4. Select the `weather_observations` table.
5. Choose `Transform Data`.
6. Confirm these data types:

| Column | Power BI Type |
| --- | --- |
| city | Text |
| latitude | Decimal number |
| longitude | Decimal number |
| temperature_c | Decimal number |
| humidity_percent | Whole number |
| precipitation_mm | Decimal number |
| wind_speed_kmh | Decimal number |
| weather_time | Date/Time |
| extracted_at | Date/Time |
| temperature_category | Text |
| rain_status | Text |

7. Set `latitude` data category to `Latitude`.
8. Set `longitude` data category to `Longitude`.

## Add Helper Columns

Create these calculated columns in Power BI:

```DAX
Observation Date = DATEVALUE(weather_observations[weather_time])
```

```DAX
Observation Hour = HOUR(weather_observations[weather_time])
```

```DAX
City Weather Label =
weather_observations[city] & " - " & weather_observations[rain_status]
```

## Add Measures

Create the measures from:

```text
powerbi/weather_dashboard_measures.dax
```

## Dashboard Page

Use a single 16:9 report page named `Weather Operations Overview`.

Import the project theme from:

```text
powerbi/weather_dashboard_theme.json
```

Suggested theme:

| Element | Color |
| --- | --- |
| Page background | `#F6F8FB` |
| Main text | `#111827` |
| Muted text | `#64748B` |
| Rain | `#2563EB` |
| No rain | `#10B981` |
| Hot temperature | `#DC2626` |
| Normal temperature | `#F59E0B` |

## Visual Layout

Top header:

```text
Malaysia Weather Operations Dashboard
Near-real-time monitoring from Python ETL, Azure Blob Storage, PostgreSQL, and Power BI
```

KPI cards:

| Card | Field |
| --- | --- |
| Avg Temp | `Latest Avg Temperature (C)` |
| Avg Humidity | `Latest Avg Humidity (%)` |
| Rainy Cities | `Latest Rainy Cities` |
| Max Wind | `Max Wind Speed (km/h)` |
| Last Refresh | `Latest Pipeline Refresh` |

Main visuals:

| Visual | Fields | Purpose |
| --- | --- | --- |
| Azure Map or Map | Latitude, Longitude, City, Rain Status, Temperature | Geographic weather monitoring |
| Clustered bar chart | City, Temperature | Rank cities by latest temperature |
| Line chart | Weather Time, Avg Temperature, City | Show temperature trend over time |
| Scatter chart | Temperature, Humidity, Precipitation, City | Compare heat, humidity, and rainfall |
| Matrix | City, Temperature, Humidity, Precipitation, Wind, Rain Status | Operational detail table |

Slicers:

| Slicer | Field |
| --- | --- |
| City | `city` |
| Rain Status | `rain_status` |
| Observation Date | `Observation Date` |

## Notes For A Strong Portfolio Screenshot

Run the pipeline multiple times before taking the screenshot. One run gives only one weather snapshot, while multiple runs make the trend line and refresh story more convincing.

After the report is ready, export or capture the dashboard image as:

```text
screenshots/powerbi_dashboard.png
```

Use this wording in your portfolio:

```text
Built a near-real-time Malaysia weather analytics dashboard using Python ETL, Azure Blob Storage, PostgreSQL, and Power BI.
```
