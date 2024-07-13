import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import SymptomAnalyzer from './components/SymptomAnalyzer';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/symptoms">
                        <SymptomAnalyzer />
                    </Route>
                    {/* Add more routes for other components */}
                </Switch>
            </div>
        </Router>
    );
}

export default App;
