import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';  // Забележи дека користиме `Routes` воместо `Switch`
import List from './List';
import Home from './Home';

const App = () => {
    return (
        <Router>
            <div className="app-container">
                <header className="app-header">
                    <h1>Welcome to the Macedonian Stock Market</h1>
                </header>
                <Routes>
                    <Route path="/" element={<Home/>}/>
                    <Route path="/list" element={<List/>}/>
                </Routes>
                <footer className="app-footer">
                    <p>&copy; 2024 Macedonian Stock Market</p>
                </footer>
            </div>
        </Router>
    );
};


export default App;
