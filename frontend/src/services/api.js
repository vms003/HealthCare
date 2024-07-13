const API_BASE_URL = 'http://localhost:5000/api';

export const analyzeSymptoms = async (symptoms) => {
    try {
        const response = await fetch(`${API_BASE_URL}/analyze_symptoms`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ symptoms })
        });
        const data = await response.json();
        return data.result;
    } catch (error) {
        console.error('Error analyzing symptoms:', error);
        return null;
    }
};

// Implement API calls for other endpoints similarly
