import React from "react";
import "./Home.css";

function Home() {
    return (
        <div className="home-container">
            <img src={`${process.env.PUBLIC_URL}/images/mareye.jpg`} alt="Mareye Zeleke Mekonen" className="profile-image" />
            <h1>Welcome to the Oil Price Dashboard</h1>
            <p>
                The main goal of this analysis is to study how important events affect Brent oil prices.
                This will focus on finding out how changes in oil prices are linked to big events like
                political decisions, conflicts in oil-producing regions, global economic sanctions, and
                changes in OPEC policies.
            </p>
        </div>
    );
}

export default Home;
