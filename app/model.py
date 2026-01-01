import pickle

model = pickle.load(open("model/model.pkl", "rb"))

def predict(study_hours, attendance):
    result = model.predict([[study_hours, attendance]])
    return "PASS" if result[0] == 1 else "FAIL"
