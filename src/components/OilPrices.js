// src/components/OilPrices.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const OilPrices = () => {
    const [oilData, setOilData] = useState([]);
    const [metrics, setMetrics] = useState({});
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchOilPrices = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/oil_prices?start_date=2023-01-01&end_date=2023-04-10');
                setOilData(response.data);
            } catch (error) {
                console.error("Error fetching oil prices:", error);
            } finally {
                setLoading(false);
            }
        };

        const fetchMetrics = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:5000/api/metrics');
                setMetrics(response.data);
            } catch (error) {
                console.error("Error fetching metrics:", error);
            }
        };

        fetchOilPrices();
        fetchMetrics();
    }, []);

    if (loading) return <div>Loading...</div>;

    const data = {
        labels: oilData.map(data => data.date),
        datasets: [
            {
                label: 'Brent Oil Prices (USD)',
                data: oilData.map(data => data.price),
                fill: false,
                borderColor: 'blue',
            },
        ],
    };

    return (
        <div>
            <h2>Brent Oil Prices Over Time</h2>
            <Line data={data} />
            <h3>Analysis Metrics</h3>
            <ul>
                {Object.entries(metrics).map(([key, value]) => (
                    <li key={key}>{key}: {value}</li>
                ))}
            </ul>
        </div>
    );
};

export default OilPrices;
