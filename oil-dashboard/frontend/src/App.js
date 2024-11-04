import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

function App() {
    const [data, setData] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5000/api/data')
            .then(response => response.json())
            .then(data => setData(data.prices.map((price, index) => ({ date: data.dates[index], price }))));
    }, []);

    return (
        <div>
            <h1>Oil Price Dashboard</h1>
            <LineChart width={600} height={300} data={data}>
                <XAxis dataKey="date" />
                <YAxis />
                <Tooltip />
                <CartesianGrid strokeDasharray="3 3" />
                <Line type="monotone" dataKey="price" stroke="#8884d8" />
            </LineChart>
        </div>
    );
}

export default App;
