const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const fraudRoutes = require('./routes/fraudRoutes');

dotenv.config();
const app = express();

app.use(express.json());
app.use('/api/fraud', fraudRoutes);

mongoose.connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));