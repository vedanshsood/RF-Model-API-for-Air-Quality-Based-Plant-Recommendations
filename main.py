import uvicorn
from fastapi import FastAPI, HTTPException
from data import Data
import pickle
import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

app = FastAPI()

# Load the model and MultiLabelBinarizer
try:
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    with open("mlb.pkl", "rb") as mlb_file:
        mlb = pickle.load(mlb_file)
except Exception as e:
    print(f"Error loading model or label binarizer: {str(e)}")
    model, mlb = None, None

# Function to predict recommended plants
def predict_recommended_plants(input_data):
    try:
        # Convert the input data to a DataFrame
        input_df = pd.DataFrame([input_data])
        print(f"Input DataFrame for Prediction:\n{input_df}")
        
        # Ensure that the columns match those used during model training
        required_features = ['PM2.5', 'PM10', 'NO', 'NO2', 'O3', 'SO2']
        if not all(feature in input_df.columns for feature in required_features):
            missing_features = [feature for feature in required_features if feature not in input_df.columns]
            raise ValueError(f"Missing features: {missing_features}")

        # Make predictions using the model
        predictions = model.predict(input_df)
        print(f"Raw Predictions (Encoded): {predictions}")

        # Decode the predictions back to plant names using MultiLabelBinarizer
        recommended_plants = mlb.inverse_transform(predictions)
        print(f"Decoded Predictions (Plant Names): {recommended_plants}")

        return recommended_plants
    except Exception as e:
        print(f"Error during prediction: {str(e)}")
        return []

@app.post("/predict")
async def predict(data: Data):
    try:
        # Convert input data to dictionary
        input_data = data.dict(by_alias=True)

        # Predict recommended plants
        recommended_plants = predict_recommended_plants(input_data)
        
        if not recommended_plants:
            raise HTTPException(status_code=500, detail="Error during prediction.")

        return {"recommended_plants": recommended_plants}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
