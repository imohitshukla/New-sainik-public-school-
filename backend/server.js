const path = require('path');
require('dotenv').config({ path: path.join(__dirname, '.env') });
const express = require('express');
const cors = require('cors');
const nodemailer = require('nodemailer');

const app = express();
const PORT = process.env.PORT || 3005;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the frontend directory
app.use(express.static(path.join(__dirname, '../frontend')));

// Configure Nodemailer using environment variables
const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_PASS
    }
});

// API endpoint for admissions inquiry
app.post('/api/inquiry', async (req, res) => {
    const { parentName, phone, email, childName, grade, message } = req.body;
    
    console.log('--- New Inquiry Received ---');
    console.log(`Parent: ${parentName}`);
    console.log(`Phone: ${phone}`);
    console.log(`Email: ${email}`);
    console.log(`Child: ${childName}`);
    console.log(`Grade: ${grade}`);
    console.log(`Message: ${message}`);
    console.log('----------------------------');

    try {
        // Send email using Nodemailer
        // NOTE: This will fail until valid credentials are provided above. 
        // We catch the error so the frontend doesn't crash during testing.
        await transporter.sendMail({
            from: `"New Sainik Public School" <${process.env.EMAIL_USER}>`,
            to: process.env.RECEIVER_EMAIL || process.env.EMAIL_USER, // School's receiving email address
            subject: `New Admissions Inquiry: ${childName} (Grade ${grade})`,
            html: `
                <h2>New Admissions Inquiry</h2>
                <p><strong>Parent Name:</strong> ${parentName}</p>
                <p><strong>Phone:</strong> ${phone}</p>
                <p><strong>Email:</strong> ${email || 'Not provided'}</p>
                <p><strong>Child's Name:</strong> ${childName}</p>
                <p><strong>Seeking Admission For:</strong> Grade ${grade}</p>
                <br/>
                <p><strong>Message / Questions:</strong></p>
                <p>${message || 'No additional message.'}</p>
            `
        });

        res.status(200).json({
            success: true,
            message: 'Thank you for your inquiry. Our admissions team will contact you shortly.'
        });
    } catch (error) {
        console.error('Error sending email:', error);
        
        // For development purposes, if email fails due to dummy credentials, 
        // we still return success to the frontend to demonstrate the UI flow.
        // In production, this should return a 500 error.
        res.status(200).json({
            success: true,
            message: 'Inquiry received (Email sending failed due to dummy credentials, but data was logged).'
        });
    }
});

// Start the server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
