const mongoose = require('mongoose');
mongoose.connect('mongodb+srv://2025ashishk_db_user:KbBdkt9DR3dpgPi6@cluster1.esms1xw.mongodb.net/?appName=Cluster1')

const db = mongoose.connection;
db.on('connected', () => {
    console.log('Database connected successfully');
});
db.on('error', (error) => {
    console.log('Database connection error:', error);
});
db.on('disconnected', () => {
    console.log('Database disconnected');
});
module.exports = db;
