const express = require('express');
const Employee = require('../models/employee');
const router = express.Router();

router.get('/', async (request, response) => {
    try {
        const employees = await Employee.find({});
        response.status(200).json(employees);
    } catch (error) {
        response.status(500).json({ message: error.message });
    }
});

router.get('/:id', async (request, response) => {
    try {
        const employee = await Employee.findById(request.params.id);
        if (!employee) {
            return response.status(404).json({ message: 'Employee not found' });
        }
        response.status(200).json(employee);
    } catch (error) {
        response.status(500).json({ message: error.message });
    }
});

router.post('/', async (request, response) => {
    try {
        const newEmployee = new Employee({
            name: request.body.name,
            email: request.body.email,
            department: request.body.department,
            salary: request.body.salary
        });
        const employee = await newEmployee.save();
        response.status(201).json(employee);
    } catch (error) {
        response.status(400).json({ message: error.message });
    }
});
router.put('/:id', async (request, response) => {
    try {
        const updatedEmployee = await Employee.findByIdAndUpdate(
            request.params.id,
            {
                name: request.body.name,
                email: request.body.email,
                department: request.body.department,
                salary: request.body.salary
            },
            { new: true }
        );
        if (!updatedEmployee) {
            return response.status(404).json({ message: 'Employee not found' });
        }
        response.status(200).json(updatedEmployee);
    }
    catch (error) {
        response.status(400).json({ message: error.message });
    }
});

router.delete('/:id', async (request, response) => {
    try {
        const employee = await Employee.findByIdAndDelete(request.params.id);
        if (!employee) {
            return response.status(404).json({ message: 'Employee not found' });
        }
        response.status(200).json({ message: 'Employee deleted successfully', employee });
    } catch (error) {
        response.status(500).json({ message: error.message });
    }
});

module.exports = router;
