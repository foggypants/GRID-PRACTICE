const express = require('express');
const cors = require('cors');
const db = require('../config/db');
const employeeRouter = require('./router/employeerouter');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());

// Routes
app.use('/employees', employeeRouter);

// Health check route
app.get('/', (req, res) => {
    res.status(200).json({ message: 'Employees API is running' });
});

// Error handling middleware
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({ message: 'Internal server error' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

module.exports = app;