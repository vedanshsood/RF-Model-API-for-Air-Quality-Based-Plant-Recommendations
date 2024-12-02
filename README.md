# 🌿 AI-Driven Plant Recommendation System

The **AI-Driven Plant Recommendation System** uses air quality metrics to recommend plants that can improve indoor air quality. Built using **FastAPI** and **Random Forest Machine Learning**, this project combines AI and sustainability to create a greener future.

---

## 🚀 Features
- **Personalized Plant Recommendations**: Based on pollutants like PM2.5, PM10, NO, NO2, O3, and SO2.
- **API Endpoint**: Seamlessly integrates with other systems.
- **Scalable and Robust**: Handles real-time prediction requests with optimized performance.

---

## 🔧 Technologies Used
- **Python**: Core programming language for development.
- **FastAPI**: For building the API.
- **scikit-learn**: To train the Random Forest model.
- **pandas**: For data manipulation.
- **Postman**: For API testing.

---

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.8 or above installed
- Required Python libraries: `pip install -r requirements.txt`

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/plant-recommendation-system.git
   cd plant-recommendation-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model (if needed):
   ```bash
   python model1.ipynb
   ```

4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

5. Test the API:
   Use **Postman** or any API testing tool. Endpoint:  
   `POST http://127.0.0.1:8000/predict`

---

## 📡 API Usage

### Endpoint
`POST /predict`

### Request Body
```json
{
    "PM2.5": 159,
    "PM10": 84,
    "NO": 6.2,
    "NO2": 11.2,
    "O3": 55.6,
    "SO2": 17.3
}
```

### Response
```json
{
    "recommended_plants": [
        ["Areca Palm", "Peace Lily", "Spider Plant"]
    ]
}
```

---

## 📂 Project Structure
```plaintext
├── main.py          # FastAPI application
├── data.py          # Input data validation using Pydantic
├── model1.ipynb     # Model training script
├── requirements.txt # Project dependencies
├── README.md        # Project documentation
```

---

## 🙌 Acknowledgments
- Thanks to the contributors of **scikit-learn** and **FastAPI** for their awesome tools.  
- Special mention to all who supported this project!





