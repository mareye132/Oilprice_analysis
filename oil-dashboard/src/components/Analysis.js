import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid, Legend } from 'recharts';

// Sample data for the chart (replace with your actual data)
const data = [
    { date: '2024-01-01', price: 80 },
    { date: '2024-02-01', price: 82 },
    { date: '2024-03-01', price: 85 },
    { date: '2024-04-01', price: 87 },
    { date: '2024-05-01', price: 90 },
    { date: '2024-06-01', price: 88 },
    { date: '2024-07-01', price: 91 },
    { date: '2024-08-01', price: 95 },
    { date: '2024-09-01', price: 93 },
    { date: '2024-10-01', price: 97 },
];

const Analysis = () => {
    return (
        <div>
            <h1>Oil Price Analysis</h1>
            <p>
                This section includes a graph that displays the relationship between Brent oil prices and their corresponding dates. 
                The line chart below illustrates the fluctuations in oil prices over the selected period, highlighting significant 
                trends and changes in the market.
            </p>
            <LineChart width={800} height={400} data={data}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Line type="monotone" dataKey="price" stroke="#8884d8" activeDot={{ r: 8 }} />
            </LineChart>
            <p>
                As seen in the chart, the Brent oil prices have experienced fluctuations due to various events such as 
                geopolitical tensions and changes in OPEC policies. For instance, notable price spikes may correspond to 
                specific political decisions or conflicts that impact oil supply and demand dynamics.
            </p>
        </div>
    );
};

export default Analysis;
