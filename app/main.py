from fastapi import FastAPI
from app.model import predict
from app.database import SessionLocal, Prediction

app = FastAPI(title="Student Performance ML API")

@app.post("/predict")
def get_prediction(study_hours: int, attendance: int):
    result = predict(study_hours, attendance)

    db = SessionLocal()
    record = Prediction(
        study_hours=study_hours,
        attendance=attendance,
        result=result
    )
    db.add(record)
    db.commit()
    db.close()

    return {
        "study_hours": study_hours,
        "attendance": attendance,
        "prediction": result
    }
