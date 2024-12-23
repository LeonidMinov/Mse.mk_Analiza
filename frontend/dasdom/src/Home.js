import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
    return (
        <div className="home-container">
            <h2 className="home-title">Welcome to the Macedonian Stock Market</h2>
            <p className="home-description">Click below to see the list of issuers:</p>
            <Link to="/list" className="home-link">See the List</Link>
        </div>
    );
}

export default Home;