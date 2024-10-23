import joblib

loaded_model = joblib.load("./model/rf_model_pipeline.pkl")


class Model():
    def Churner(data):
        prediction = loaded_model.predict(data)
        if prediction == 1:
            return "Don't worry about this one"
        else:
            return "Churner! Attetion"