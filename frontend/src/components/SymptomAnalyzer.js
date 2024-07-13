import React, { useState } from 'react';
import { analyzeSymptoms } from '../services/api';

const SymptomAnalyzer = () => {
    const [symptoms, setSymptoms] = useState('');
    const [analysisResult, setAnalysisResult] = useState('');

    const handleAnalysis = async () => {
        const result = await analyzeSymptoms(symptoms);
        setAnalysisResult(result);
    };

    return (
        <div>
            <h2>Symptom Analyzer</h2>
            <textarea
                placeholder="Enter symptoms..."
                value={symptoms}
                onChange={(e) => setSymptoms(e.target.value)}
            />
            <button onClick={handleAnalysis}>Analyze Symptoms</button>
            {analysisResult && <p>Analysis Result: {analysisResult}</p>}
        </div>
    );
};

export default SymptomAnalyzer;
